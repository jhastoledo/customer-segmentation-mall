# ╔══════════════════════════════════════════════════════════════════╗
# ║  inject_dark_theme.py                                            ║
# ║  Aplica tema dark premium em HTML exportado pelo nbconvert       ║
# ║                                                                  ║
# ║  USO:                                                            ║
# ║    from inject_dark_theme import aplicar_tema_dark               ║
# ║    aplicar_tema_dark("reports/relatorio_final.html")             ║
# ╚══════════════════════════════════════════════════════════════════╝

from pathlib import Path


# ── CSS premium injetado no <head> ────────────────────────────────
_DARK_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════════
   PREMIUM DARK THEME — nbconvert HTML (JupyterLab output)
   Paleta GitHub Dark Dimmed · Fonte Inter + JetBrains Mono
   ═══════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:ital,wght@0,400;0,500;1,400&display=swap');

/* ── Variáveis de design ──────────────────────────────────────── */
:root {
    --bg-base:       #0d1117;
    --bg-surface:    #161b22;
    --bg-elevated:   #1c2128;
    --bg-hover:      #1f2937;
    --border:        #30363d;
    --border-subtle: #21262d;

    --text-primary:  #e6edf3;
    --text-secondary:#8b949e;
    --text-muted:    #6e7681;

    --accent-blue:   #58a6ff;
    --accent-purple: #d2a8ff;
    --accent-green:  #3fb950;
    --accent-orange: #ffa657;
    --accent-red:    #ff7b72;
    --accent-cyan:   #79c0ff;
    --accent-yellow: #e3b341;

    --cell-radius:   8px;
    --font-ui:       'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono:     'JetBrains Mono', 'Fira Mono', 'Consolas', monospace;

    /* Sobrescreve variáveis internas do JupyterLab */
    --jp-cell-editor-background:         #161b22;
    --jp-cell-editor-active-background:  #1c2128;
    --jp-mirror-editor-keyword-color:    #ff7b72;
    --jp-mirror-editor-string-color:     #a5d6ff;
    --jp-mirror-editor-number-color:     #d2a8ff;
    --jp-mirror-editor-comment-color:    #6e7681;
    --jp-mirror-editor-variable-color:   #e6edf3;
    --jp-mirror-editor-operator-color:   #79c0ff;
    --jp-mirror-editor-builtin-color:    #ffa657;
    --jp-mirror-editor-def-color:        #d2a8ff;
    --jp-mirror-editor-error-color:      #ff7b72;
    --jp-mirror-editor-punctuation-color:#e6edf3;
    --jp-mirror-editor-meta-color:       #ffa657;
    --jp-layout-color0:                  #161b22;
    --jp-rendermime-table-row-background:#1c2128;
    --jp-rendermime-table-row-hover-background: #1f2937;
    --jp-border-color1:                  #30363d;
    --jp-border-width:                   1px;
}

*, *::before, *::after { box-sizing: border-box; }

/* ── Base ─────────────────────────────────────────────────────── */
html, body {
    background-color: var(--bg-base) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-ui) !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
}

/* ── Container principal ─────────────────────────────────────── */
#notebook-container,
.jp-Notebook,
div#notebook {
    background-color: var(--bg-base) !important;
    padding: 40px 24px !important;
    max-width: 980px !important;
    margin: 0 auto !important;
    box-shadow: none !important;
}

/* ── Células ──────────────────────────────────────────────────── */
.jp-Cell, .jp-CodeCell, .jp-MarkdownCell,
div.cell, div.code_cell, div.text_cell {
    background-color: transparent !important;
    border: none !important;
    margin: 0 0 6px !important;
    padding: 0 !important;
    position: relative;
}
.jp-Cell + .jp-Cell,
div.cell + div.cell { margin-top: 8px !important; }

/* ── Input area (código) ──────────────────────────────────────── */
.jp-InputArea,
div.input,
div.input_area {
    background-color: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--cell-radius) !important;
    margin: 2px 0 0 18px !important;
    padding: 0 !important;
    overflow: hidden;
    transition: border-color .2s, box-shadow .2s;
}
.jp-InputArea:hover, div.input:hover {
    border-color: #4d5763 !important;
    box-shadow: 0 2px 12px rgba(0,0,0,.3) !important;
}

/* ── Prompt ───────────────────────────────────────────────────── */
.jp-InputPrompt, .jp-OutputPrompt,
div.input_prompt, div.output_prompt, div.prompt {
    font-family: var(--font-mono) !important;
    font-size: 11px !important;
    color: var(--text-muted) !important;
    background-color: transparent !important;
    min-width: 64px !important;
    padding: 12px 10px !important;
    text-align: right !important;
    user-select: none;
    opacity: 1 !important;
    border-right: 1px solid var(--border-subtle) !important;
}

/* ── Editor de código ─────────────────────────────────────────── */
.CodeMirror, .cm-s-ipython, .jp-CodeMirrorEditor {
    font-family: var(--font-mono) !important;
    font-size: 13px !important;
    line-height: 1.65 !important;
    background-color: var(--bg-surface) !important;
    color: var(--text-primary) !important;
    border-radius: 0 !important;
    height: auto !important;
    padding: 12px 16px !important;
}
.CodeMirror-gutters,
.cm-s-ipython .CodeMirror-gutters {
    background-color: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
}
.CodeMirror-linenumber,
.cm-s-ipython .CodeMirror-linenumber {
    color: var(--text-muted) !important;
    font-size: 11px !important;
}

/* ── Syntax highlighting — CodeMirror ────────────────────────── */
.cm-s-ipython span.cm-keyword    { color: #ff7b72 !important; font-weight: 500 !important; }
.cm-s-ipython span.cm-string,
.cm-s-ipython span.cm-string-2   { color: #a5d6ff !important; }
.cm-s-ipython span.cm-number,
.cm-s-ipython span.cm-atom       { color: #d2a8ff !important; }
.cm-s-ipython span.cm-comment    { color: #8b949e !important; font-style: italic !important; }
.cm-s-ipython span.cm-builtin    { color: #ffa657 !important; }
.cm-s-ipython span.cm-def        { color: #d2a8ff !important; font-weight: 500 !important; }
.cm-s-ipython span.cm-variable   { color: var(--text-primary) !important; }
.cm-s-ipython span.cm-variable-2 { color: #79c0ff !important; }
.cm-s-ipython span.cm-variable-3 { color: #ffa657 !important; }
.cm-s-ipython span.cm-operator   { color: #79c0ff !important; }
.cm-s-ipython span.cm-meta       { color: #ffa657 !important; }
.cm-s-ipython span.cm-tag        { color: #7ee787 !important; }
.cm-s-ipython span.cm-error      { color: #ff7b72 !important; background: rgba(255,123,114,.15) !important; }

/* ── Syntax highlighting — Pygments (HTML exportado) ─────────── */
.highlight                        { background: var(--bg-surface) !important; }
.highlight .k,  .highlight .kd,
.highlight .kn, .highlight .kp,
.highlight .kr, .highlight .kt   { color: #ff7b72 !important; font-weight: 500 !important; }
.highlight .s,  .highlight .s1,
.highlight .s2, .highlight .sb,
.highlight .sc, .highlight .sd,
.highlight .sh, .highlight .si,
.highlight .ss                   { color: #a5d6ff !important; }
.highlight .m,  .highlight .mb,
.highlight .mf, .highlight .mh,
.highlight .mi, .highlight .mo,
.highlight .il                   { color: #d2a8ff !important; }
.highlight .c,  .highlight .c1,
.highlight .cm, .highlight .cp,
.highlight .cs, .highlight .ch   { color: #8b949e !important; font-style: italic !important; }
.highlight .nb                   { color: #ffa657 !important; }
.highlight .nf                   { color: #d2a8ff !important; }
.highlight .nc                   { color: #f0883e !important; }
.highlight .nn                   { color: #79c0ff !important; }
.highlight .o,  .highlight .ow   { color: #79c0ff !important; }
.highlight .nd                   { color: #ffa657 !important; }
.highlight .na                   { color: #79c0ff !important; }
.highlight .err                  { color: #ff7b72 !important;
                                   background: rgba(255,123,114,.08) !important;
                                   border: none !important; }

/* ── Output area ──────────────────────────────────────────────── */
.jp-OutputArea,
.jp-OutputArea-output,
div.output_area,
div.output_subarea,
div.output_text,
div.output_wrapper {
    background-color: var(--bg-base) !important;
    color: var(--text-primary) !important;
    border: none !important;
    margin-left: 18px !important;
}
.jp-RenderedText pre,
div.output_text pre,
.jp-OutputArea-output pre {
    font-family: var(--font-mono) !important;
    font-size: 12.5px !important;
    line-height: 1.6 !important;
    color: var(--text-primary) !important;
    background-color: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--cell-radius) !important;
    padding: 12px 16px !important;
    margin: 4px 0 !important;
    overflow-x: auto !important;
}
.jp-RenderedText[data-mime-type="application/vnd.jupyter.stderr"] pre,
div.output-stderr pre {
    background-color: rgba(255,123,114,.06) !important;
    border-color: rgba(255,123,114,.25) !important;
    color: #ffa198 !important;
}

/* ── Markdown ─────────────────────────────────────────────────── */
.jp-MarkdownOutput, .jp-RenderedHTMLCommon,
div.text_cell_render {
    font-family: var(--font-ui) !important;
    color: var(--text-primary) !important;
    background-color: transparent !important;
    padding: 14px 20px 14px 26px !important;
    line-height: 1.8 !important;
}

/* ── Headings ─────────────────────────────────────────────────── */
.jp-RenderedHTMLCommon h1, div.text_cell_render h1 {
    font-size: 1.9rem !important; font-weight: 700 !important;
    color: var(--accent-blue) !important;
    border-bottom: 2px solid var(--border) !important;
    padding-bottom: 10px !important; margin: 28px 0 16px !important;
    letter-spacing: -.02em;
}
.jp-RenderedHTMLCommon h2, div.text_cell_render h2 {
    font-size: 1.45rem !important; font-weight: 600 !important;
    color: var(--accent-cyan) !important;
    border-bottom: 1px solid var(--border-subtle) !important;
    padding-bottom: 5px !important; margin: 24px 0 12px !important;
}
.jp-RenderedHTMLCommon h3, div.text_cell_render h3 {
    font-size: 1.15rem !important; font-weight: 600 !important;
    color: var(--accent-purple) !important;
    margin: 20px 0 10px !important;
}
.jp-RenderedHTMLCommon h4, div.text_cell_render h4 {
    font-size: 1rem !important; font-weight: 600 !important;
    color: var(--accent-orange) !important;
    margin: 16px 0 8px !important;
}
.anchor-link { opacity: 0; transition: opacity .2s; font-size: .75em; margin-left: 6px; }
h1:hover .anchor-link, h2:hover .anchor-link, h3:hover .anchor-link { opacity: .4; }

/* ── Parágrafos e listas ──────────────────────────────────────── */
.jp-RenderedHTMLCommon p,   div.text_cell_render p   { color: var(--text-primary) !important; margin: 8px 0 !important; }
.jp-RenderedHTMLCommon ul,  div.text_cell_render ul,
.jp-RenderedHTMLCommon ol,  div.text_cell_render ol  { color: var(--text-primary) !important; padding-left: 1.6em !important; }
.jp-RenderedHTMLCommon li,  div.text_cell_render li  { margin: 4px 0 !important; }

/* ── Blockquote ───────────────────────────────────────────────── */
.jp-RenderedHTMLCommon blockquote, div.text_cell_render blockquote {
    border-left: 4px solid var(--accent-blue) !important;
    background-color: var(--bg-elevated) !important;
    color: var(--text-secondary) !important;
    padding: 10px 16px !important;
    border-radius: 0 6px 6px 0 !important;
    margin: 12px 0 !important;
}

/* ── Code inline ──────────────────────────────────────────────── */
.jp-RenderedHTMLCommon code, div.text_cell_render code {
    font-family: var(--font-mono) !important;
    font-size: .875em !important;
    background-color: var(--bg-elevated) !important;
    color: var(--accent-orange) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    padding: 2px 6px !important;
}

/* ══════════════════════════════════════════════════════════════
   TABELAS — corrige table-layout: fixed nativo + sobreposição
   ══════════════════════════════════════════════════════════════ */

/* 1. Wrapper com scroll horizontal — evita que a tabela quebre o layout */
.jp-RenderedHTMLCommon table,
div.text_cell_render table,
.dataframe,
.rendered_html table {
    /* Anula o table-layout: fixed do nbconvert que causa sobreposição */
    table-layout: auto !important;
    border-collapse: collapse !important;
    width: 100% !important;
    font-family: var(--font-mono) !important;
    font-size: 12.5px !important;
    margin: 12px 0 !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--cell-radius) !important;
    overflow: visible !important; /* o scroll fica no wrapper abaixo */
    box-shadow: 0 2px 10px rgba(0,0,0,.35) !important;
    color: var(--text-primary) !important;
}

/* 2. Células de cabeçalho */
.jp-RenderedHTMLCommon thead th,
div.text_cell_render thead th,
.dataframe thead th,
.rendered_html thead th {
    background: linear-gradient(135deg, #1c2128 0%, #21262d 100%) !important;
    color: var(--accent-blue) !important;
    font-weight: 600 !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: .06em !important;
    padding: 10px 16px !important;
    border-bottom: 2px solid var(--accent-blue) !important;
    border-right: 1px solid var(--border) !important;
    text-align: left !important;
    /* garante quebra de linha ao invés de transbordar */
    white-space: normal !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
}
.jp-RenderedHTMLCommon thead th:last-child,
.dataframe thead th:last-child,
.rendered_html thead th:last-child { border-right: none !important; }

/* 3. Células de dados */
.jp-RenderedHTMLCommon tbody td,
div.text_cell_render tbody td,
.dataframe tbody td,
.rendered_html tbody td {
    background-color: var(--bg-surface) !important;
    color: var(--text-primary) !important;
    padding: 9px 16px !important;
    border-bottom: 1px solid var(--border-subtle) !important;
    border-right: 1px solid var(--border-subtle) !important;
    /* palavras longas nunca transbordam para a célula vizinha */
    white-space: normal !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    vertical-align: top !important;
    line-height: 1.55 !important;
}
.jp-RenderedHTMLCommon tbody td:last-child,
.dataframe tbody td:last-child,
.rendered_html tbody td:last-child { border-right: none !important; }

/* 4. Zebra e hover */
.jp-RenderedHTMLCommon tbody tr:nth-child(even) td,
.dataframe tbody tr:nth-child(even) td,
.rendered_html tbody tr:nth-child(even) td {
    background-color: var(--bg-elevated) !important;
}
.jp-RenderedHTMLCommon tbody tr:hover td,
.dataframe tbody tr:hover td,
.rendered_html tbody tr:hover td {
    background-color: var(--bg-hover) !important;
}

/* 5. Wrapper de scroll — envolve a tabela para rolar em vez de vazar */
.jp-OutputArea-output .jp-RenderedHTMLCommon,
div.output_area .rendered_html {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
}

/* ── Imagens ──────────────────────────────────────────────────── */
.jp-RenderedImage img,
div.output_png img,
div.output_jpeg img {
    border-radius: var(--cell-radius) !important;
    border: 1px solid var(--border) !important;
    max-width: 100% !important;
    display: block !important;
    margin: 8px auto !important;
    box-shadow: 0 4px 20px rgba(0,0,0,.45) !important;
}

/* ── Links ────────────────────────────────────────────────────── */
a { color: var(--accent-blue) !important; text-decoration: none !important; }
a:hover { color: var(--accent-cyan) !important; text-decoration: underline !important; }

/* ── Scrollbar ────────────────────────────────────────────────── */
::-webkit-scrollbar              { width: 7px; height: 7px; }
::-webkit-scrollbar-track        { background: var(--bg-base); }
::-webkit-scrollbar-thumb        { background: var(--border); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover  { background: var(--accent-blue); }

/* ── ANSI colors (stdout colorido) ───────────────────────────── */
.ansi-bold                  { font-weight: 700 !important; }
.ansi-red-fg,    .ansired   { color: #ff7b72 !important; }
.ansi-green-fg,  .ansigreen { color: #3fb950 !important; }
.ansi-yellow-fg, .ansiyellow{ color: #e3b341 !important; }
.ansi-blue-fg,   .ansiblue  { color: #58a6ff !important; }
.ansi-magenta-fg,.ansipurple{ color: #d2a8ff !important; }
.ansi-cyan-fg,   .ansicyan  { color: #79c0ff !important; }
.ansi-bright-green-fg       { color: #56d364 !important; }
.ansi-bright-blue-fg        { color: #79c0ff !important; }

/* ── Responsivo ───────────────────────────────────────────────── */
@media (max-width: 768px) {
    #notebook-container, .jp-Notebook, div#notebook { padding: 16px !important; }
    .jp-InputArea, div.input   { margin-left: 8px !important; }
    .jp-OutputArea, div.output_area { margin-left: 8px !important; }
}
</style>
"""


def aplicar_tema_dark(
    html_path: str | Path,
    output_path: str | Path | None = None,
    sobrescrever: bool = False,
) -> Path:
    """Injeta o tema dark premium num HTML exportado pelo nbconvert.

    Parâmetros
    ----------
    html_path : str | Path
        Caminho do HTML gerado pelo nbconvert (entrada).

    output_path : str | Path | None
        Caminho de saída. Se None, gera '<nome>_dark.html' no mesmo
        diretório que o arquivo de entrada.

    sobrescrever : bool
        Se True e output_path == html_path, sobrescreve o original.
        Padrão False para evitar perda de dados.

    Retorna
    -------
    Path
        Caminho do arquivo HTML com o tema aplicado.

    Exemplos
    --------
    # Forma mais simples — salva em reports/relatorio_final_dark.html
    from inject_dark_theme import aplicar_tema_dark
    aplicar_tema_dark("reports/relatorio_final.html")

    # Especificando a saída
    aplicar_tema_dark(
        "reports/relatorio_final.html",
        output_path="reports/relatorio_final.html",
        sobrescrever=True,          # substitui o próprio arquivo
    )
    """
    html_path = Path(html_path)

    if not html_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {html_path}")
    if not html_path.suffix.lower() == ".html":
        raise ValueError(f"O arquivo precisa ser .html, recebeu: {html_path.suffix}")

    # Define destino
    if output_path is None:
        out = html_path.with_name(html_path.stem + "_dark.html")
    else:
        out = Path(output_path)

    if out == html_path and not sobrescrever:
        raise ValueError(
            "output_path é igual ao html_path. "
            "Passe sobrescrever=True para substituir o original."
        )

    # Lê, injeta, salva
    html = html_path.read_text(encoding="utf-8")

    if "</head>" not in html:
        raise ValueError("HTML inválido: tag </head> não encontrada.")

    html_dark = html.replace("</head>", _DARK_CSS + "\n</head>", 1)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_dark, encoding="utf-8")

    tamanho_kb = out.stat().st_size / 1024
    print(f"✅ Tema dark aplicado com sucesso!")
    print(f"   → {out}")
    print(f"   Tamanho: {tamanho_kb:.1f} KB")

    return out
