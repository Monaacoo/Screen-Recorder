# Screen Recorder

Este projeto é um gravador de tela simples desenvolvido em Python utilizando as bibliotecas OpenCV e PyAutoGUI.

## Pré-requisitos

Antes de executar o código, certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install opencv-python pyautogui numpy
```

## Como funciona

O script captura continuamente a tela do usuário, converte os quadros para o formato RGB e os grava em um arquivo de vídeo (`Recording.mp4`). O processo pode ser interrompido pressionando a tecla `q`.

## Configurações

- **Resolução:** 1920x1080 (pode ser alterada na variável `reso`).
- **Codec:** `CLCO` (pode ser ajustado conforme necessário).
- **FPS:** 70.0 quadros por segundo (ajustável na variável `fps`).
- **Nome do arquivo de saída:** `Recording.mp4`.
- **Janela de pré-visualização:** Redimensionada para 500x400 pixels.

## Como executar

Execute o script Python com o seguinte comando:

```bash
python main.py
```

Para interromper a gravação, pressione `q`.

## Observação

- Certifique-se de que o codec `CLCO` está disponível no seu sistema. Se necessário, altere para outro codec compatível.
- O desempenho pode variar dependendo da taxa de FPS e da resolução selecionada.
