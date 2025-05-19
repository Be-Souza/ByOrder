# 🖨️ ByOrder – Impressão de Ordens de Serviço via Serial

**ByOrder** é um sistema desktop minimalista e funcional, desenvolvido para facilitar a impressão de Ordens de Serviço diretamente em impressoras térmicas Bematech, utilizando a porta serial (COM).  
O sistema foi criado para uso interno em setores de **T.I**, otimizando o processo de registro e documentação de atendimento técnico.

---

## ✨ Funcionalidades

✅ Interface gráfica intuitiva com **CustomTkinter** (modo escuro)  
✅ Impressão direta em impressoras seriais com **corte automático de papel**  
✅ Seleção de porta COM através de menu de configurações ⚙️  
✅ Campos opcionais para **economia** de espaço em bobina de impressão 
✅ Marcação de **prioridade** da OS (Baixa, Média, Alta)  
✅ Geração de **ID único** para cada OS  
✅ Armazenamento local (ou em rede) das OSs geradas em arquivos `.txt`  
✅ Codificação compatível com impressoras térmicas (**CP437**)  
✅ Notificações de sucesso e falha com mensagens ao usuário  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [pyserial](https://pythonhosted.org/pyserial/)
- Tkinter (widgets complementares)
- Impressora térmica Bematech (via porta COM)

---

## 🗂️ Estrutura de Salvamento

Cada OS gerada é automaticamente salva como um arquivo `.txt` em uma pasta configurável no sistema, podendo ser local ou de rede.  
Isso facilita a **rastreamento**, **auditoria** e **compartilhamento** das ordens emitidas.

---

## 🧠 Motivação

Este projeto surgiu da necessidade real de **automatizar e padronizar** a emissão de Ordens de Serviço técnicas em uma empresa, com foco na **agilidade**, **simplicidade de uso** e **compatibilidade com o hardware existente**.

---

## 📌 Observações

> Compatível com impressoras térmicas **Bematech** (testado com porta COM física).  
> Recomendado para ambientes Windows com suporte a drivers seriais.

---

## 📎 Licença

Este projeto pode ser utilizado e adaptado livremente para fins não-comerciais.  
Para usos empresariais ou distribuição, entre em contato com o autor.

---
