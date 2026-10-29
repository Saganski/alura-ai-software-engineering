#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Moderna em Python
Implementação com operações fundamentais (soma, subtração, multiplicação, divisão)
e histórico de cálculos persistente.
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
        op = operador.strip()
        simbolo = op

        try:
            if op in ('+', 'soma', 'somar'):
                resultado_float = self.somar(a, b)
                simbolo = '+'
            elif op in ('-', '−', 'subtracao', 'subtrair'):
                resultado_float = self.subtrair(a, b)
                simbolo = '−'
            elif op in ('*', 'x', 'X', '×', 'multiplicacao', 'multiplicar'):
                resultado_float = self.multiplicar(a, b)
                simbolo = '×'
            elif op in ('/', '÷', 'divisao', 'dividir'):
                resultado_float = self.dividir(a, b)
                simbolo = '÷'
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

        except ZeroDivisionError:
            str_a = self.formatar_numero(a)
            return {
                "sucesso": False,
                "erro": "Não é possível dividir por zero",
                "expressao": f"{str_a} ÷ 0",
                "resultado": "Erro: Divisão por 0"
            }
        except Exception as e:
            return {
                "sucesso": False,
                "erro": str(e),
                "expressao": f"{a} {operador} {b}",
                "resultado": "Erro"
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
    print("=" * 45)
    print("       CALCULADORA MODERNA EM PYTHON")
    print("=" * 45)
    print("Operações disponíveis:")
    print("  +  : Soma")
    print("  -  : Subtração")
    print("  *  : Multiplicação")
    print("  /  : Divisão")
    print("  h  : Ver Histórico")
    print("  c  : Limpar Histórico")
    print("  s  : Sair")
    print("-" * 45)

    while True:
        try:
            comando = input("\nDigite a operação (ex: 15 + 7) ou 's' para sair: ").strip()
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

            # Tenta dividir a expressão em 3 partes: num1 operador num2
            partes = comando.split()
            if len(partes) != 3:
                print("Formato inválido! Use: <número> <operador> <número> (ex: 25 * 4)")
                continue

            n1 = float(partes[0].replace(',', '.'))
            operador = partes[1]
            n2 = float(partes[2].replace(',', '.'))

            resultado = calc.calcular(n1, operador, n2)
            if resultado["sucesso"]:
                print(f"=> Resultado: {resultado['resultado']}")
            else:
                print(f"=> {resultado.get('erro', 'Erro no cálculo')}")

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
