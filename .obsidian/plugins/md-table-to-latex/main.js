"use strict";
Object.defineProperty(exports, "__esModule", { value: true });

const obsidian = require("obsidian");

class TitleInputModal extends obsidian.Modal {
  constructor(app) {
    super(app);
    this.result = null;
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.createEl("h3", { text: "输入表格标题" });

    const input = contentEl.createEl("input", {
      type: "text",
      placeholder: "例如：表1：主要变量描述性统计",
    });
    input.style.width = "100%";
    input.style.marginBottom = "12px";
    input.focus();

    const btnContainer = contentEl.createDiv();
    btnContainer.style.display = "flex";
    btnContainer.style.gap = "8px";
    btnContainer.style.justifyContent = "flex-end";

    const cancelBtn = btnContainer.createEl("button", { text: "取消" });
    cancelBtn.addEventListener("click", () => this.close());

    const confirmBtn = btnContainer.createEl("button", { text: "确定" });
    confirmBtn.style.backgroundColor = "var(--interactive-accent)";
    confirmBtn.style.color = "var(--text-on-accent)";

    const onSubmit = () => {
      this.result = input.value.trim();
      this.close();
    };
    confirmBtn.addEventListener("click", onSubmit);
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") onSubmit();
    });
  }

  onClose() {
    const { contentEl } = this;
    contentEl.empty();
  }

  async waitForTitle() {
    return new Promise((resolve) => {
      this.open();
      // 监听 close 事件
      const origClose = this.close.bind(this);
      this.close = () => {
        origClose();
        resolve(this.result);
      };
    });
  }
}

class MdTableToLatexPlugin extends obsidian.Plugin {
  async onload() {
    this.addCommand({
      id: "convert-markdown-table-to-latex",
      name: "Convert Markdown Table to LaTeX",
      editorCallback: async (editor) => {
        await this.convertSelection(editor);
      },
    });

    this.addRibbonIcon("table-2", "Markdown 表格转 LaTeX", async () => {
      const view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
      if (!view) {
        new obsidian.Notice("请先在编辑器中打开笔记");
        return;
      }
      await this.convertSelection(view.editor);
    });
  }

  async convertSelection(editor) {
    const selected = editor.getSelection();
    if (!selected) {
      new obsidian.Notice("请先选中一个 Markdown 表格");
      return;
    }

    const modal = new TitleInputModal(this.app);
    const title = await modal.waitForTitle();
    if (title === null) return;

    const result = this.convert(selected, title);
    if (result) {
      editor.replaceSelection(result);
      new obsidian.Notice("已转换为 LaTeX 表格");
    } else {
      new obsidian.Notice("无法识别选中的内容为 Markdown 表格");
    }
  }

  convert(text, title) {
    const lines = text.split("\n").filter((l) => l.trim() !== "");
    if (lines.length < 2) return null;

    const sepIdx = lines.findIndex((l) => /^\|?\s*:?-{3,}:?\s*/.test(l.trim()));
    if (sepIdx === -1) return null;

    const sepLine = lines[sepIdx].replace(/^\||\|$/g, "");
    const alignList = sepLine.split("|").map((p) => {
      const t = p.trim();
      if (t.startsWith(":") && t.endsWith(":")) return "c";
      if (t.endsWith(":")) return "r";
      if (t.startsWith(":")) return "l";
      return "c";
    });

    const strip = (s) => s.replace(/\$/g, "");

    const headerLine = lines[sepIdx - 1];
    if (!headerLine) return null;
    const header = headerLine.replace(/^\||\|$/g, "").split("|").map((c) => strip(c.trim()));

    const dataLines = lines.slice(sepIdx + 1);
    const body = dataLines.map((l) =>
      l.replace(/^\||\|$/g, "").split("|").map((c) => strip(c.trim())).join(" & ")
    );

    const alignStr = alignList.join("");
    const headerStr = header.join(" & ");

    const tableBody = "\\begin{array}{" + alignStr + "}\n" +
      "\\hline\n" +
      headerStr + " \\\\\n" +
      "\\hline\n" +
      body.join(" \\\\\n") + " \\\\\n" +
      "\\hline\n" +
      "\\end{array}";

    let latex;
    if (title) {
      latex = "$$\n\\begin{array}{c}\n\\text{" + title + "} \\\\[4pt]\n" +
        tableBody + "\n" +
        "\\end{array}\n$$";
    } else {
      latex = "$$\n" + tableBody + "\n$$";
    }

    return latex;
  }
}

module.exports = MdTableToLatexPlugin;

/* nosourcemap */