import os
import platform
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("=" * 60)
print("🔍 VERIFICANDO CHROMEDRIVER")
print("=" * 60)

print(f"🖥️  Sistema Operacional: {platform.system()}")
print(f"📍 Python: {platform.python_version()}")
print(f"🏗️  Arquitetura: {platform.machine()}")

try:
    print("\n⏳ Localizando ChromeDriver...")
    driver_path = ChromeDriverManager().install()
    print(f"✅ ChromeDriver encontrado: {driver_path}")
    
    print("\n⏳ Inicializando Chrome...")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    print(f"✅ Chrome inicializado com sucesso!")
    
    print(f"📊 Versão do Chrome: {driver.capabilities['browserVersion']}")
    print(f"🔧 Versão do WebDriver: {driver.capabilities['chrome']['chromedriverVersion']}")
    
    driver.quit()
    print("\n✅ ChromeDriver funcional!")
    
    print("\n" + "=" * 60)
    print("✅ TESTE DE CHROMEDRIVER PASSOU!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Erro ao inicializar Chrome: {e}")
    print("\n" + "=" * 60)
    print("💡 SOLUÇÕES:")
    print("=" * 60)
    print("  1. Instale/atualize Chrome:")
    print("     - Windows: https://www.google.com/chrome/")
    print("     - Linux: sudo apt-get install google-chrome-stable")
    print("     - Mac: brew install google-chrome")
    print("\n  2. Execute: pip install --upgrade webdriver-manager")
    print("\n  3. Limpe cache:")
    print("     - Windows: rmdir /s %UserProfile%\\.wdm")
    print("     - Linux/Mac: rm -rf ~/.wdm/")
    print("=" * 60)