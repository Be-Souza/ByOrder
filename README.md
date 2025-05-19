# ByOrder
🖨️ ByOrder – Impressão de Ordens de Serviço com Python e Serial
Sistema desktop para geração e impressão de Ordens de Serviço utilizado no setor de T.I da CR Diementz. Desenvolvido com Python e CustomTkinter, possui integração com impressoras Bematech via porta serial (COM), permitindo impressão direta de OSs com corte automático de papel.

Principais funcionalidades:
Interface gráfica responsiva com CustomTkinter (modo escuro);

Impressão de OSs em impressoras térmicas seriais (Bematech);

Seleção dinâmica da porta COM detectada;

Geração automática de IDs únicos para cada OS;

Salvamento local das OSs geradas em arquivos .txt;

Campos opcionais para IP, patrimônio e observações;

Suporte a diferentes níveis de prioridade;

Tratamento de erros e mensagens de status ao usuário.

Tecnologias utilizadas:
Python 3.11+

CustomTkinter

pyserial

Tkinter / CTkOptionMenu / CTkTextbox

Codificação CP437 para impressoras térmicas

