# Estratégia PDF Downloader

Automação local para baixar os PDFs **originais** das aulas disponíveis na sessão autenticada do usuário. Não solicita senha ao CLI, não contorna autenticação ou controles de acesso e usa a URL assinada que a própria página da aula apresenta.

## Requisitos

- Python 3.10+
- Playwright para Python e Chromium

## Instalação

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Uso

Na primeira execução, o Chromium abre visível. Faça login manualmente no Estratégia e aguarde o scraper continuar. O perfil fica salvo em `browser-profile/` para retomar a execução sem inserir senha no programa.

```powershell
python scraper.py --course "https://www.estrategiaconcursos.com.br/app/dashboard/pacote/384948" --output .\downloads
```

Opções: `--headless`, `--resume`, `--max-retries`, `--delay`, `--timeout` e `--profile`. Use `--headless` apenas após autenticar e salvar a sessão no perfil persistente.

Os arquivos ficam em pastas numeradas por matéria. `progress.json` registra cada aula e `logs/errors.log` mantém falhas detalhadas. A execução é sequencial, com pausa configurável entre navegações e downloads. Uma nova execução valida PDFs existentes e continua o progresso.

## Estrutura do projeto

- `scraper.py`: CLI e coordenação
- `browser.py`: perfil persistente e contexto autenticado
- `crawler.py`: descoberta de cursos e aulas a partir dos links renderizados
- `downloader.py`: extração do link original e validação do PDF
- `selectors.py`: seletores observados/configuráveis
- `progress.py`: estado retomável
- `utils.py`: nomes seguros e verificação da assinatura PDF

