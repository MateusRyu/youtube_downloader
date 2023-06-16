# YouTube Downloader
Este é um aplicativo simples feito em Python com a biblioteca 
PySimpleGUI e o pytube que permite baixar vídeos MP4 ou áudios MP3 de um 
link informado pelo usuário.
Requisitos
Certifique-se de ter o Python instalado em seu sistema.

## Instalação das dependências
Para instalar as dependências necessárias, siga as etapas abaixo:
1. Faça o download ou clone este repositório em seu sistema.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde 
você salvou o aplicativo.
3. Execute o seguinte comando para instalar as dependências:
``` bash
# Esse comando irá ler o arquivo requirements.txt e instalar todas as 
bibliotecas necessárias.
pip install -r requirements.txt
```

## Como executar o aplicativo
1. Certifique-se de ter instalado todas as dependências mencionadas 
acima.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde 
você salvou o aplicativo.
3. Execute o seguinte comando para iniciar o aplicativo:
4. python app.py
5. A interface gráfica será exibida. Informe o link do vídeo ou áudio 
que você deseja baixar e selecione o tipo de mídia (Vídeo MP4 ou Áudio 
MP3).
6. Clique no botão "Baixar" para iniciar o processo de download.
7. Após o download ser concluído, uma mensagem de sucesso será exibida.

## Observações
 O arquivo baixado será salvo com um nome padrão (downloaded_media.mp4 
 ou downloaded_media.mp3) dentro da pasta downloads e na pasta adequada 
 para audio ou video, dentro do mesmo diretório onde o script está 
 localizado. Caso você queira alterar o nome ou local do arquivo, você 
 pode editar a variável output_path no código.
 Certifique-se de ter permissões de escrita no diretório onde o script 
 está localizado, pois é onde o arquivo baixado será salvo.
 Este aplicativo utiliza o pytube como biblioteca para fazer o download 
 dos vídeos/áudios. Certifique-se de que o link fornecido seja 
 compatível com o pytube.

Espero que este aplicativo seja útil para você! Se você tiver alguma 
dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em 
contato através do e-mail 
[suporte.ryu@gmail.com](mailto:suporte.ryu@gmail.com)!
