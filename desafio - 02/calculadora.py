#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Científica em Python
Implementação com operações fundamentais (+, -, *, /), exponenciação (^),
raiz quadrada e n-ésima, porcentagem (%), gerador de gráficos de funções f(x)
com Matplotlib e histórico de cálculos persistente.
"""

import sys
import json
import math
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

HISTORICO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "historico_calculos.json")


class Calculadora:
    """Classe responsável pelas regras de negócio e operações matemáticas."""

    def __init__(self, persistir: bool = True):
        self.persistir = persistir
        self.historico: List[Dict[str, Any]] = []
        if self.persistir:
            self.carregar_historico()

    def somar(self, a: float, b: float) -> float:
        """Realiza a soma entre dois números."""
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        """Realiza a subtração entre dois números."""
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Realiza a multiplicação entre dois números."""
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Realiza a divisão entre dois números.
        Lança ZeroDivisionError se b == 0.
        """
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não permitida")
        return a / b

    def exponenciar(self, base: float, expoente: float) -> float:
        """Realiza a exponenciação (base elevada ao expoente)."""
        return base ** expoente

    def raiz(self, radicando: float, indice: float = 2.0) -> float:
        """
        Calcula a raiz de um número (por padrão, raiz quadrada).
        Lança ValueError para raízes de índice par com radicando negativo.
        """
        if indice == 0:
            raise ZeroDivisionError("Índice da raiz não pode ser zero")
        if radicando < 0 and indice % 2 == 0:
            raise ValueError("Não existe raiz real para radicando negativo com índice par")
        if radicando < 0:
            return -((-radicando) ** (1.0 / indice))
        return radicando ** (1.0 / indice)

    def porcentagem(self, total: float, percentual: float) -> float:
        """Calcula o percentual de um valor (ex: 15% de 200 = 30)."""
        return (total * percentual) / 100.0

    def formatar_numero(self, valor: float) -> str:
        """
        Formata o número eliminando imprecisões de ponto flutuante
        e zeros desnecessários no final.
        """
        if math.isnan(valor):
            return "Erro"
        if math.isinf(valor):
            return "Erro: Infinito"

        # Arredonda para 10 casas decimais para evitar 0.1 + 0.2 = 0.30000000000000004
        arredondado = round(valor, 10)
        
        # Se for um número inteiro exato
        if arredondado.is_integer():
            return str(int(arredondado))
        
        # Representação científica para números extremos
        if abs(arredondado) > 1e12 or (0 < abs(arredondado) < 1e-6):
            return f"{arredondado:.6e}"

        # Remove zeros à direita após o ponto decimal
        texto = f"{arredondado:.10f}".rstrip("0").rstrip(".")
        return texto

    def calcular(self, a: float, operador: str, b: float) -> Dict[str, Any]:
        """
        Executa a operação matemática, formata e armazena no histórico.
        """
        op = operador.strip().lower()
        simbolo = op

        try:
            if op in ('+', 'soma', 'somar'):
                resultado_float = self.somar(a, b)
                simbolo = '+'
            elif op in ('-', '−', 'subtracao', 'subtrair'):
                resultado_float = self.subtrair(a, b)
                simbolo = '−'
            elif op in ('*', 'x', '×', 'multiplicacao', 'multiplicar'):
                resultado_float = self.multiplicar(a, b)
                simbolo = '×'
            elif op in ('/', '÷', 'divisao', 'dividir'):
                resultado_float = self.dividir(a, b)
                simbolo = '÷'
            elif op in ('^', '**', 'potencia', 'exp', 'exponenciacao'):
                resultado_float = self.exponenciar(a, b)
                simbolo = '^'
            elif op in ('%', 'porcento', 'porcentagem'):
                resultado_float = self.porcentagem(a, b)
                simbolo = '%'
            elif op in ('raiz', 'sqrt', '√', 'v'):
                resultado_float = self.raiz(a, b)
                simbolo = f"√[{self.formatar_numero(b)}]"
            else:
                return {
                    "sucesso": False,
                    "erro": f"Operador inválido: '{operador}'",
                    "expressao": f"{a} {operador} {b}",
                    "resultado": "Erro"
                }

            resultado_formatado = self.formatar_numero(resultado_float)
            str_a = self.formatar_numero(a)
            str_b = self.formatar_numero(b)
            expressao = f"{str_a} {simbolo} {str_b}"

            item_historico = {
                "id": f"{int(datetime.now().timestamp() * 1000)}",
                "expressao": expressao,
                "resultado": resultado_formatado,
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "a": a,
                "operador": simbolo,
                "b": b,
                "resultado_numerico": resultado_float
            }

            self.historico.insert(0, item_historico)
            # Limita a 100 itens mais recentes
            self.historico = self.historico[:100]

            if self.persistir:
                self.salvar_historico()

            return {
                "sucesso": True,
                "expressao": expressao,
                "resultado": resultado_formatado,
                "item": item_historico
            }

        except ZeroDivisionError as zde:
            str_a = self.formatar_numero(a)
            return {
                "sucesso": False,
                "erro": str(zde) if str(zde) else "Divisão por zero não permitida",
                "expressao": f"{str_a} {simbolo} {self.formatar_numero(b)}",
                "resultado": "Erro: Divisão por 0"
            }
        except ValueError as ve:
            return {
                "sucesso": False,
                "erro": str(ve),
                "expressao": f"{self.formatar_numero(a)} {simbolo} {self.formatar_numero(b)}",
                "resultado": "Erro: Valor Inválido"
            }
        except OverflowError:
            return {
                "sucesso": False,
                "erro": "Resultado excede o limite numérico (Overflow)",
                "expressao": f"{self.formatar_numero(a)} {simbolo} {self.formatar_numero(b)}",
                "resultado": "Erro: Infinito/Overflow"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "erro": str(e),
                "expressao": f"{a} {operador} {b}",
                "resultado": "Erro"
            }

    def calcular_unario(self, operador: str, valor: float) -> Dict[str, Any]:
        """
        Executa operações com um único valor (ex: raiz quadrada 'raiz 25', percentual '15 %').
        """
        op = operador.strip().lower()
        simbolo = op

        try:
            if op in ('raiz', 'sqrt', '√', 'v'):
                resultado_float = self.raiz(valor, 2.0)
                simbolo = '√'
                expressao = f"√{self.formatar_numero(valor)}"
            elif op in ('%', 'porcento', 'porcentagem'):
                resultado_float = valor / 100.0
                simbolo = '%'
                expressao = f"{self.formatar_numero(valor)}%"
            else:
                return {
                    "sucesso": False,
                    "erro": f"Operação unária inválida: '{operador}'",
                    "expressao": f"{operador} {valor}",
                    "resultado": "Erro"
                }

            resultado_formatado = self.formatar_numero(resultado_float)

            item_historico = {
                "id": f"{int(datetime.now().timestamp() * 1000)}",
                "expressao": expressao,
                "resultado": resultado_formatado,
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "a": valor,
                "operador": simbolo,
                "b": None,
                "resultado_numerico": resultado_float
            }

            self.historico.insert(0, item_historico)
            self.historico = self.historico[:100]

            if self.persistir:
                self.salvar_historico()

            return {
                "sucesso": True,
                "expressao": expressao,
                "resultado": resultado_formatado,
                "item": item_historico
            }

        except ValueError as ve:
            return {
                "sucesso": False,
                "erro": str(ve),
                "expressao": f"{simbolo}{self.formatar_numero(valor)}",
                "resultado": "Erro: Raiz Inválida"
            }
        except OverflowError:
            return {
                "sucesso": False,
                "erro": "Resultado excede o limite numérico (Overflow)",
                "expressao": f"{simbolo}{self.formatar_numero(valor)}",
                "resultado": "Erro: Overflow"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "erro": str(e),
                "expressao": f"{operador} {valor}",
                "resultado": "Erro"
            }

    def plotar_grafico(self, expressao_funcao: str, x_min: float = -10.0, x_max: float = 10.0, pontos: int = 500) -> Dict[str, Any]:
        """
        Gera um gráfico científico interativo de uma função f(x) utilizando matplotlib.
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            return {
                "sucesso": False,
                "erro": (
                    "A biblioteca 'matplotlib' não está instalada no ambiente.\n"
                    "Para visualizar gráficos científicos, instale-a executando no terminal:\n"
                    "    pip install matplotlib"
                )
            }

        if x_min >= x_max:
            return {
                "sucesso": False,
                "erro": "O valor inicial de X (x_min) deve ser menor que o valor final (x_max)."
            }

        # Dicionário de funções matemáticas seguras para avaliação
        escopo_seguro = {
            "__builtins__": {},
            "sin": math.sin,
            "sen": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "raiz": math.sqrt,
            "abs": abs,
            "log": math.log,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
        }

        # Substitui notações amigáveis como ^ por **
        expressao_limpa = expressao_funcao.strip().replace("^", "**")

        passo = (x_max - x_min) / max(pontos - 1, 1)
        x_valores = [x_min + i * passo for i in range(pontos)]
        y_valores = []

        sucesso_pelo_menos_um = False
        for x in x_valores:
            escopo_seguro["x"] = x
            try:
                y = eval(expressao_limpa, escopo_seguro)
                if isinstance(y, (int, float)) and not math.isnan(y) and not math.isinf(y):
                    # Evita estourar o gráfico com valores astronômicos (ex: assíntotas verticais)
                    if abs(y) > 1e7:
                        y_valores.append(float('nan'))
                    else:
                        y_valores.append(float(y))
                        sucesso_pelo_menos_um = True
                else:
                    y_valores.append(float('nan'))
            except (ZeroDivisionError, ValueError, OverflowError):
                y_valores.append(float('nan'))
            except Exception as e:
                return {
                    "sucesso": False,
                    "erro": f"Erro na sintaxe da função f(x): {e}"
                }

        if not sucesso_pelo_menos_um:
            return {
                "sucesso": False,
                "erro": "Nenhum valor real válido pôde ser calculado para a função no intervalo indicado."
            }

        try:
            fig, ax = plt.subplots(figsize=(9, 5.5))
            ax.plot(x_valores, y_valores, label=f"f(x) = {expressao_funcao}", color="#0066cc", linewidth=2.2)

            # Eixos cartesianos X e Y
            ax.axhline(0, color="#333333", linewidth=1.1, linestyle="--", alpha=0.7)
            ax.axvline(0, color="#333333", linewidth=1.1, linestyle="--", alpha=0.7)

            ax.grid(True, linestyle=":", alpha=0.6)
            ax.set_title(f"Gráfico Científico: f(x) = {expressao_funcao}", fontsize=13, fontweight="bold", pad=12)
            ax.set_xlabel("Eixo X", fontsize=11)
            ax.set_ylabel("f(x)", fontsize=11)
            ax.legend(loc="best", frameon=True)
            plt.tight_layout()

            print("Abrindo janela do gráfico (feche a janela do gráfico para continuar no terminal)...")
            plt.show()

            return {"sucesso": True, "funcao": expressao_funcao}
        except Exception as e:
            return {
                "sucesso": False,
                "erro": f"Falha ao exibir o gráfico: {e}"
            }

    def limpar_historico(self) -> None:
        """Limpa todo o histórico de cálculos."""
        self.historico.clear()
        if self.persistir and os.path.exists(HISTORICO_FILE):
            try:
                os.remove(HISTORICO_FILE)
            except OSError:
                pass

    def salvar_historico(self) -> None:
        """Salva o histórico em formato JSON."""
        try:
            with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
                json.dump(self.historico, f, ensure_ascii=False, indent=2)
        except Exception as e:
            sys.stderr.write(f"Aviso: Não foi possível salvar histórico: {e}\n")

    def carregar_historico(self) -> None:
        """Carrega o histórico existente do arquivo JSON."""
        if os.path.exists(HISTORICO_FILE):
            try:
                with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
                    self.historico = json.load(f)
            except Exception:
                self.historico = []


# ==========================================
# Interface de Linha de Comando (CLI)
# ==========================================
def executar_cli():
    calc = Calculadora()
    print("=" * 50)
    print("       CALCULADORA CIENTÍFICA EM PYTHON")
    print("=" * 50)
    print("Operações disponíveis:")
    print("  +    : Soma             (ex: 15 + 7)")
    print("  -    : Subtração        (ex: 20 - 8)")
    print("  *    : Multiplicação    (ex: 6 * 7)")
    print("  /    : Divisão          (ex: 10 / 2)")
    print("  ^    : Exponenciação    (ex: 2 ^ 8)")
    print("  raiz : Raiz             (ex: raiz 25 ou 8 raiz 3)")
    print("  %    : Porcentagem      (ex: 200 % 15 ou 15 %)")
    print("  g    : Gráfico de f(x)  (abre janela interativa)")
    print("  h    : Ver Histórico")
    print("  c    : Limpar Histórico")
    print("  s    : Sair")
    print("-" * 50)

    while True:
        try:
            comando = input("\nDigite a operação (ex: 15 + 7, raiz 25) ou 's' para sair: ").strip()
            if not comando:
                continue

            if comando.lower() in ('s', 'sair', 'exit', 'quit'):
                print("Encerrando calculadora. Até mais!")
                break

            if comando.lower() in ('h', 'historico'):
                if not calc.historico:
                    print("[Histórico vazio]")
                else:
                    print("\n--- HISTÓRICO DE CÁLCULOS ---")
                    for i, item in enumerate(calc.historico, 1):
                        print(f"{i}. {item['expressao']} = {item['resultado']}  ({item['timestamp']})")
                continue

            if comando.lower() in ('c', 'limpar'):
                calc.limpar_historico()
                print("Histórico limpo com sucesso!")
                continue

            # Comando para plotar gráfico de função
            if comando.lower() in ('g', 'grafico', 'graficos', 'plot'):
                print("\n--- GERADOR DE GRÁFICO CIENTÍFICO ---")
                print("Exemplos de funções: x**2 - 4, sin(x), 2*x + 1, cos(x)*2, sqrt(x)")
                func_str = input("Digite a função f(x): ").strip()
                if not func_str:
                    print("Operação cancelada.")
                    continue

                x_min_str = input("Digite o valor inicial de X [Padrão: -10]: ").strip()
                x_max_str = input("Digite o valor final de X [Padrão: 10]: ").strip()

                try:
                    x_min = float(x_min_str.replace(',', '.')) if x_min_str else -10.0
                    x_max = float(x_max_str.replace(',', '.')) if x_max_str else 10.0
                except ValueError:
                    print("Valores de intervalo inválidos. Usando padrão [-10, 10].")
                    x_min, x_max = -10.0, 10.0

                resultado_grafico = calc.plotar_grafico(func_str, x_min, x_max)
                if not resultado_grafico["sucesso"]:
                    print(f"=> {resultado_grafico.get('erro', 'Erro ao gerar gráfico')}")
                else:
                    print("=> Gráfico gerado com sucesso!")
                continue

            # Casos com símbolo direto colado (ex: √25 ou 15%)
            if comando.startswith('√') and len(comando) > 1:
                val = float(comando[1:].strip().replace(',', '.'))
                resultado = calc.calcular_unario('√', val)
                if resultado["sucesso"]:
                    print(f"=> Resultado: {resultado['resultado']}")
                else:
                    print(f"=> {resultado.get('erro', 'Erro no cálculo')}")
                continue

            if comando.endswith('%') and len(comando) > 1 and not (' ' in comando):
                val = float(comando[:-1].strip().replace(',', '.'))
                resultado = calc.calcular_unario('%', val)
                if resultado["sucesso"]:
                    print(f"=> Resultado: {resultado['resultado']}")
                else:
                    print(f"=> {resultado.get('erro', 'Erro no cálculo')}")
                continue

            partes = comando.split()

            # Operação com 2 partes (ex: "raiz 25", "sqrt 9", "15 %")
            if len(partes) == 2:
                if partes[0].lower() in ('raiz', 'sqrt', '√', 'v'):
                    val = float(partes[1].replace(',', '.'))
                    resultado = calc.calcular_unario(partes[0], val)
                elif partes[1] in ('%', 'porcento', 'porcentagem'):
                    val = float(partes[0].replace(',', '.'))
                    resultado = calc.calcular_unario(partes[1], val)
                else:
                    print("Formato inválido! Para raiz quadrada use: raiz <número> (ex: raiz 25)")
                    continue

                if resultado["sucesso"]:
                    print(f"=> Resultado: {resultado['resultado']}")
                else:
                    print(f"=> {resultado.get('erro', 'Erro no cálculo')}")
                continue

            # Operação com 3 partes (ex: "25 * 4", "2 ^ 8", "200 % 15", "8 raiz 3")
            if len(partes) == 3:
                n1 = float(partes[0].replace(',', '.'))
                operador = partes[1]
                n2 = float(partes[2].replace(',', '.'))

                resultado = calc.calcular(n1, operador, n2)
                if resultado["sucesso"]:
                    print(f"=> Resultado: {resultado['resultado']}")
                else:
                    print(f"=> {resultado.get('erro', 'Erro no cálculo')}")
                continue

            print("Formato inválido! Exemplos válidos:")
            print("  - Operações: 25 * 4, 2 ^ 8, 200 % 15, 8 raiz 3")
            print("  - Raiz quadrada: raiz 25")
            print("  - Porcentagem direta: 15 %")
            print("  - Gráficos de funções: digite 'g'")

        except ValueError:
            print("Erro: Certifique-se de digitar números válidos.")
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break


# ==========================================
# Modo JSON (para integração com API / Web)
# ==========================================
def processar_json_argumento():
    if len(sys.argv) > 2 and sys.argv[1] == "--eval":
        try:
            dados = json.loads(sys.argv[2])
            a = float(dados["a"])
            op = str(dados["op"])
            b = float(dados["b"])

            calc = Calculadora()
            resultado = calc.calcular(a, op, b)
            print(json.dumps(resultado, ensure_ascii=False))
            sys.exit(0)
        except Exception as e:
            print(json.dumps({"sucesso": False, "erro": str(e)}, ensure_ascii=False))
            sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[1] == "--eval-unario":
        try:
            dados = json.loads(sys.argv[2])
            op = str(dados["op"])
            valor = float(dados["valor"])

            calc = Calculadora()
            resultado = calc.calcular_unario(op, valor)
            print(json.dumps(resultado, ensure_ascii=False))
            sys.exit(0)
        except Exception as e:
            print(json.dumps({"sucesso": False, "erro": str(e)}, ensure_ascii=False))
            sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[1] == "--plot":
        try:
            dados = json.loads(sys.argv[2])
            func = str(dados.get("func", "x"))
            x_min = float(dados.get("x_min", -10))
            x_max = float(dados.get("x_max", 10))

            calc = Calculadora()
            resultado = calc.plotar_grafico(func, x_min, x_max)
            print(json.dumps(resultado, ensure_ascii=False))
            sys.exit(0)
        except Exception as e:
            print(json.dumps({"sucesso": False, "erro": str(e)}, ensure_ascii=False))
            sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == "--historico":
        calc = Calculadora()
        print(json.dumps(calc.historico, ensure_ascii=False))
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == "--limpar-historico":
        calc = Calculadora()
        calc.limpar_historico()
        print(json.dumps({"sucesso": True}, ensure_ascii=False))
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("--"):
        processar_json_argumento()
    else:
        executar_cli()
