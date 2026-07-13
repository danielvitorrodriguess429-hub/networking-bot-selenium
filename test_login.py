import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("🔐 TESTE DE LOGIN NO LINKEDIN")
print("=" * 60)

email = os.getenv('LINKEDIN_EMAIL')
senha = os.getenv('LINKEDIN_SENHA')

if not email or not senha:
    print("❌ Configure LINKEDIN_EMAIL e LINKEDIN_SENHA no .env")
    print("\n📝 Execute primeiro: python test_env.py")
    sys.exit(1)

print(f"📧 Email: {email[:3]}***{email[-3:]}")
print(f"🔑 Senha: {'*' * len(senha)}")

try:
    print("\n" + "=" * 60)
    print("🚀 INICIANDO TESTE DE LOGIN")
    print("=" * 60)
    
    print("\n⏳ Iniciando navegador Chrome...")
    options = Options()
    # Remover --headless para ver o navegador
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    print("✅ Chrome iniciado!")
    
    print("\n📍 Acessando https://www.linkedin.com/login...")
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)
    
    print("📝 Preenchendo email...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_field.clear()
    email_field.send_keys(email)
    time.sleep(1)
    print("✅ Email preenchido!")
    
    print("🔑 Preenchendo senha...")
    senha_field = driver.find_element(By.ID, "password")
    senha_field.clear()
    senha_field.send_keys(senha)
    time.sleep(1)
    print("✅ Senha preenchida!")
    
    print("🔓 Clicando em login...")
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    print("✅ Botão clicado!")
    
    print("\n⏳ Aguardando redirecionamento (10 segundos)...")
    time.sleep(10)
    
    current_url = driver.current_url
    
    print("\n" + "=" * 60)
    print("📊 RESULTADO DO TESTE")
    print("=" * 60)
    print(f"📍 URL atual: {current_url}")
    
    # Verificar se login foi bem-sucedido
    sucesso = False
    
    if "login" not in current_url.lower():
        print("✅ Redirecionado (saiu da página de login)")
        sucesso = True
    else:
        print("⚠️  Ainda na página de login")
    
    # Tentar localizar elemento de feed
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//nav//button"))
        )
        print("✅ Elementos da página carregados!")
        sucesso = True
    except:
        print("⚠️  Não foi possível localizar elementos (pode ser CAPTCHA)")
    
    print("\n" + "=" * 60)
    if sucesso:
        print("✅ LOGIN PROVAVELMENTE BEM-SUCEDIDO!")
        print("=" * 60)
        print("\n💡 Próximo passo: python test_search.py")
    else:
        print("⚠️  VERIFICAR MANUALMENTE NO NAVEGADOR")
        print("=" * 60)
        print("\n💡 Possíveis causas:")
        print("  - CAPTCHA apareceu (resolva manualmente)")
        print("  - 2FA ativado (desative temporariamente)")
        print("  - Credenciais incorretas")
        print("  - LinkedIn bloqueou a conta")
        print("\n⏸️  Pressione ENTER para fechar...")
        input()
    
    driver.quit()
    
except Exception as e:
    print(f"\n❌ ERRO NO TESTE DE LOGIN:")
    print(f"   {type(e).__name__}: {e}")
    print("\n" + "=" * 60)
    print("💡 POSSÍVEIS SOLUÇÕES:")
    print("=" * 60)
    print("  1. Credenciais incorretas?")
    print("     - Verifique email e senha no .env")
    print("\n  2. 2FA ativado?")
    print("     - Desative em Configurações > Segurança")
    print("\n  3. LinkedIn detectou atividade suspeita?")
    print("     - Aguarde 24 horas")
    print("\n  4. CAPTCHA?")
    print("     - Faça login manual e use cookies")
    print("=" * 60)
    
    try:
        driver.quit()
    except:
        pass