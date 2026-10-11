import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.join(os.environ["USERPROFILE"], ".gemini", "antigravity", "tec_browser_data")
os.makedirs(USER_DATA_DIR, exist_ok=True)

def main():
    print(f"[Login] Iniciando navegador com perfil persistente em: {USER_DATA_DIR}", flush=True)
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            channel="chrome",
            headless=False,
            viewport={"width": 1280, "height": 850},
            args=["--start-maximized"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        
        print("[Login] Navegando para página de login do TecConcursos...", flush=True)
        page.goto("https://www.tecconcursos.com.br/login", wait_until="domcontentloaded")
        time.sleep(2)
        
        screenshot_path = os.path.join(os.environ["USERPROFILE"], ".gemini", "antigravity", "tec_login_screen.png")
        page.screenshot(path=screenshot_path)
        print(f"[Login] Screenshot inicial salvo em: {screenshot_path}", flush=True)
        
        print("\n=======================================================", flush=True)
        print("Janela do navegador ABERTA na tela do usuário.", flush=True)
        print("Aguardando login diretamente pela interface do site...", flush=True)
        print("=======================================================\n", flush=True)
        
        while True:
            time.sleep(2)
            try:
                curr_url = page.url
                # Se não estiver mais na página de login e não tiver botão de entrar
                if "login" not in curr_url.lower():
                    has_login_btn = page.locator("a:has-text('Entrar'), button:has-text('Entrar')").count() > 0
                    if not has_login_btn:
                        print(f"\n[Login] Sucesso! Usuário autenticado na URL: {curr_url}", flush=True)
                        time.sleep(5)
                        break
            except Exception as e:
                pass
                
        print("[Login] Sessão persistida com sucesso no diretório de perfil.", flush=True)
        context.close()

if __name__ == "__main__":
    main()
