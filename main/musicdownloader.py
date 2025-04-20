import yt_dlp
import os
from tkinter import *
from tkinter import messagebox

#criando pasta de download
os.makedirs('C:\Musicas-Python', exist_ok=True)

def baixar_audio():
    print("função chamada!")
    link = entrada_link.get()
    if not link:
        messagebox.showwarning("Aviso", "Insira um link válido")
        return
        print(f"Baixando musica do link: {link}")

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': 'C:\Musicas-Python/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'C:\Users\samnu\ffmpeg-7.1.1-full_build\bin'

    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Sucesso, musica baixa com sucesso.")
    except Exception as e:
        import traceback
        erro = traceback.format_exc()
        print("erro", e)
        messagebox.showerror("Erro", f"Erro ao baixar: {str(e)}")

# interface grafica

janela = Tk()
janela.title("Downloadeando audio")
janela.geometry("400x150")

Label(janela, text="Link do vídeo, pia: ").pack(pady=10)
entrada_link = Entry(janela, width=50)
entrada_link.pack()

Button(janela, text="Baixar audio MP3", command=baixar_audio).pack(pady=10)

janela.mainloop()