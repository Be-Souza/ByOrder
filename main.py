import customtkinter as ctk
import serial
import serial.tools.list_ports
from datetime import datetime
from tkinter import messagebox
import os
import json

# Porta COM selecionada (padrão COM4)
porta_com = "COM4"

def gerar_id_os():
    caminho_id = r"\\192.168.0.65\backup1\ByOrder\os_data\id_os.json"
    os.makedirs(os.path.dirname(caminho_id), exist_ok=True)

    if os.path.exists(caminho_id):
        with open(caminho_id, 'r') as f:
            data = json.load(f)
            ultimo_id = data.get("ultimo_id", 0)
    else:
        ultimo_id = 0

    novo_id = ultimo_id + 1

    with open(caminho_id, 'w') as f:
        json.dump({"ultimo_id": novo_id}, f)

    return f"OS{novo_id:05d}"

def imprimir_os():
    try:
        global porta_com
        filial = entry_filial.get()
        patrimonio = entry_patrimonio.get()
        equipamento = entry_equipamento.get()
        ip = entry_ip.get()
        problema = text_problema.get("1.0", "end").strip()
        obs = entry_obs.get()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        prioridade = prioridade_var.get()
        id_os = gerar_id_os()

        texto = "\n"
        texto += "-" * 50 + "\n"
        texto += "  ORDEM DE SERVIÇO - CR DIEMENTZ\n"
        texto += "-" * 50 + "\n"
        texto += f"ID: {id_os}\n"
        texto += f"Data/Hora: {data_hora}\n"
        texto += f"Filial: {filial}\n"
        texto += f"Prioridade: {prioridade}\n"
        if patrimonio:
            texto += f"Patrimônio: {patrimonio}\n"
        texto += f"Equipamento: {equipamento}\n"
        if ip:
            texto += f"IP: {ip}\n"
        if obs:
            texto += f"OBS: {obs}\n"
        texto += "-" * 50 + "\n"
        texto += "Problema Relatado:\n"
        texto += f"{problema}\n"
        texto += "-" * 50 + "\n"
        texto += "Téc. Responsável: ________________________\n"
        texto += "[ ] Resolvido\n"
        texto += "-" * 50 + "\n\n\n"

        # Impressão direta com corte total (mais garantido em Bematech)
        porta = serial.Serial(porta_com, 9600)
        porta.write(texto.encode('cp437', errors='replace'))
        porta.write(b'\x1B\x69')  # Corte total (Bematech)
        porta.close()

        salvar_arquivo_os(id_os, texto)

        print(texto)
        messagebox.showinfo("Sucesso", "OS enviada para impressão!")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao imprimir: {e}")

def salvar_arquivo_os(id_os, texto):
    pasta_destino = r"\\192.168.0.65\backup1\ByOrder\OS"
    os.makedirs(pasta_destino, exist_ok=True)

    caminho_arquivo = os.path.join(pasta_destino, f"{id_os}.txt")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)

def abrir_configuracoes():
    def salvar_porta():
        global porta_com
        porta_com = combo.get()
        janela_config.destroy()

    janela_config = ctk.CTkToplevel(janela)
    janela_config.title("Configurações")
    janela_config.geometry("340x150")

    label = ctk.CTkLabel(janela_config, text="Selecionar Porta COM:")
    label.pack(pady=(20, 10))

    portas = [port.device for port in serial.tools.list_ports.comports()]
    combo = ctk.CTkOptionMenu(janela_config, values=portas)
    combo.pack(pady=5)

    combo.set(porta_com)  # Define a atual
    btn_salvar = ctk.CTkButton(janela_config, text="Salvar", command=salvar_porta)
    btn_salvar.pack(pady=10)

# Interface gráfica
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("ByOrder - Suporte T.I (CR Diementz)")
janela.geometry("340x675")
janela.resizable(False, False)

def criar_label(texto):
    label = ctk.CTkLabel(janela, text=texto)
    label.pack(pady=(10, 0), anchor='w', padx=20)

def criar_entry():
    return ctk.CTkEntry(janela, width=300)

def criar_text(altura):
    text = ctk.CTkTextbox(janela, width=300, height=altura)
    text.bind("<Tab>", lambda e: focar_proximo(e))
    return text

def focar_proximo(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Campos do formulário
criar_label("Filial:")
entry_filial = criar_entry()
entry_filial.pack(fill='x', pady=5, padx=20)

criar_label("Patrimônio (opcional):")
entry_patrimonio = criar_entry()
entry_patrimonio.pack(fill='x', pady=5, padx=20)

criar_label("Equipamento:")
entry_equipamento = criar_entry()
entry_equipamento.pack(fill='x', pady=5, padx=20)

criar_label("IP (opcional):")
entry_ip = criar_entry()
entry_ip.pack(fill='x', pady=5, padx=20)

criar_label("OBS (opcional):")
entry_obs = criar_entry()
entry_obs.pack(fill='x', pady=5, padx=20)

criar_label("Problema Relatado:")
text_problema = criar_text(100)
text_problema.pack(fill='x', pady=5, padx=20)

criar_label("Prioridade:")
prioridades = ["Baixa", "Média", "Alta"]
prioridade_var = ctk.StringVar(value="Média")  # valor padrão
entry_prioridade = ctk.CTkOptionMenu(janela, variable=prioridade_var, values=prioridades)
entry_prioridade.pack(fill='x', pady=5, padx=20)

btn_imprimir = ctk.CTkButton(janela, text="Imprimir OS", command=imprimir_os)
btn_imprimir.pack(pady=20)

btn_config = ctk.CTkButton(janela, text="⚙️", width=30, command=abrir_configuracoes)
btn_config.place(x=300, y=10)

janela.mainloop()
