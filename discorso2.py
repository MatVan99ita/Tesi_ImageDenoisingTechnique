import pypandoc

# Testo LaTeX da convertire in plain text
latex_text = r"""
\section*{Discorso di presentazione tesi}

\begin{enumerate}
    \item \textbf{Introduzione} \\
    Mi chiamo Matteo Vanni e oggi presento la mia tesi: 
    \emph{Analisi comparativa di modelli di Deep Learning per la riduzione del rumore in immagini digitali}. 
    Gli obiettivi sono: comprendere il problema del rumore, analizzare modelli deep learning, confrontarli su dataset reali e sintetici, evidenziandone punti di forza e limiti.

    \item \textbf{Cos’è il denoising} \\
    È il processo di rimozione del rumore per migliorare la qualità visiva e supportare analisi automatiche. 
    Esistono vari tipi di rumore: Gaussiano, Poissoniano, Salt-and-Pepper, Speckle, rumore reale da sensori.

    \item \textbf{Metodi tradizionali} \\
    - Filtri mediani e gaussiani. \\
    - Non-Local Means e BM3D come riferimenti classici. \\
    Limiti: perdita di dettagli, poca flessibilità.

    \item \textbf{Metodi deep learning} \\
    - Reti neurali convoluzionali (DnCNN, RIDNet). \\
    - Approcci auto-supervisionati come Noise2Noise. \\
    - GAN e modelli più recenti.

    \item \textbf{Architetture considerate} \\
    - RIDNet: rete modulare con attenzione sui canali e apprendimento residuo. \\
    - DnCNN: rete profonda di 20 strati, apprende direttamente il rumore. \\
    - Autoencoder: compressione + ricostruzione, meno performante.

    \item \textbf{Dataset utilizzati} \\
    - SIDD, Renoir: rumore reale. \\
    - BSD500, DIV2K, FiveK: rumore sintetico a vari livelli. \\
    - Kvasir: dataset medico per valutare la generalizzazione.

    \item \textbf{Preprocessing} \\
    Operazioni di padding e patching a risoluzione 512x512. 
    Aggiunta di rumore artificiale (σ=15,25,50). 
    Divisione dataset in training e validation.

    \item \textbf{Sperimentazione} \\
    Training con ottimizzatore Adam e loss MSE. 
    Confronto con BM3D come baseline classica.

    \item \textbf{Risultati principali} \\
    - RIDNet: migliore su quasi tutti i dataset, robusto anche con rumore elevato. \\
    - DnCNN: prestazioni intermedie, degrada con alto rumore. \\
    - Autoencoder: il meno performante. \\
    - BM3D: valido solo a basso rumore. \\
    Caso particolare: su dataset Scacchi, RidNet e BM3D equivalenti.

    \item \textbf{Fine tuning su Kvasir} \\
    Necessario per specializzare i modelli a immagini mediche. 
    Miglioramento visibile per RidNet e DnCNN, più limitato per l’Autoencoder.

    \item \textbf{Conclusioni} \\
    RidNet risulta il modello più versatile e robusto. 
    Il fine tuning è fondamentale per domini specifici. 
    Possibili sviluppi futuri: modelli transformer, approcci auto-supervised e applicazioni cliniche.
\end{enumerate}
"""

# Conversione in testo semplice
txt_output = pypandoc.convert_text(latex_text, 'plain', format='latex')

# Salvataggio come file .txt
output_path = "/mnt/data/discorso_tesi.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(txt_output)

output_path
