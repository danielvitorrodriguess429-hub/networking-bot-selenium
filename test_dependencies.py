import sys
import importlib

print("=" * 60)
print("🧪 VERIFICANDO DEPENDÊNCIAS")
print("=" * 60)

dependencias = {
    'selenium': 'selenium',
    'dotenv': 'dotenv',
    'webdriver_manager': 'webdriver_manager'
}

todos_ok = True

for nome_display, nome_modulo in dependencias.items():
    try:
        mod = importlib.import_module(nome_modulo)
        versao_atual = getattr(mod, '__version__', 'N/A')
        print(f"✅ {nome_display:20} v{versao_atual:10} - OK")
    except ImportError:
        print(f"❌ {nome_display:20} - NÃO INSTALADO")
        todos_ok = False

print("\n" + "=" * 60)
if todos_ok:
    print("✅ TODAS AS DEPENDÊNCIAS INSTALADAS!")
    print("=" * 60)
    sys.exit(0)
else:
    print("❌ INSTALE AS DEPENDÊNCIAS COM:")
    print("   pip install -r requirements.txt")
    print("=" * 60)
    sys.exit(1)