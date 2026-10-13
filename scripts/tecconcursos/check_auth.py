import os
import sys
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.join(os.environ["USERPROFILE"], ".gemini", "antigravity", "tec_browser_data")
os.makedirs(USER_DATA_DIR, exist_ok=True)

def main():
    print(f"Iniciando navegador com perfil persistente em: {USER_DATA_DIR}")
    with sync_playwright() as p:
        # Abre o navegador visível (headless=False)
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            channel="chrome",  # usa o Chrome instalado se disponível, ou fallback para chromium
            headless=False,
            viewport={"width": 1280, "height": 800},
            args=["--start-maximized"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        
        print("Acessando TecConcursos...")
        page.goto("https://www.tecconcursos.com.br/questoes/cadernos", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        
        current_url = page.url
        page_title = page.title()
        print(f"URL atual: {current_url}")
        print(f"Título da página: {page_title}")
        
        # Verifica se está autenticado
        # No TecConcursos, se não estiver autenticado, geralmente redireciona para login ou exibe botão 'Entrar'
        is_login_page = "login" in current_url.lower() or "entrar" in current_url.lower()
        has_login_button = page.locator("a:has-text('Entrar'), button:has-text('Entrar'), a[href*='login']").count() > 0
        has_user_menu = page.locator(".user-menu, [aria-label*='perfil'], a[href*='logout'], a[href*='sair'], .avatar").count() > 0
        
        print(f"is_login_page: {is_login_page}")
        print(f"has_login_button: {has_login_button}")
        print(f"has_user_menu: {has_user_menu}")
        
        screenshot_path = os.path.join(os.environ["USERPROFILE"], ".gemini", "antigravity", "tec_status.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot salvo em: {screenshot_path}")

        if is_login_page or has_login_button or not has_user_menu:
            print("\nSTATUS: NÃO AUTENTICADO. Por favor, realize o login na janela do navegador que foi aberta.")
            # Deixa o navegador aberto aguardando interação do usuário ou fecha context se for script rápido
        else:
            print("\nSTATUS: AUTENTICADO COM SUCESSO!")
            
        context.close()

if __name__ == "__main__":
    main()
