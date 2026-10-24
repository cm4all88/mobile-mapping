/* ===========================================================================
   The record sheet, and the words that go with it.

   This file is injected into BOTH the tablet app and the office intake page, so
   a record looks the same wherever it is opened and nobody has to keep two
   renderers in step. It reads a record and nothing else: no storage, no DOM
   beyond the string it returns.
   =========================================================================== */
const LOGO = "{{LOGO}}";
const esc = s => String(s == null ? "" : s)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const pad = n => String(n).padStart(2, "0");
const when = t => t ? new Date(t).toLocaleString() : "";
function transferWords(t){
  if (!t) return "not sent";
  if (t.status === "sent") return "delivery confirmed " + when(t.sentAt);
  if (t.status === "handed") return "handed over " + when(t.handedAt) + ", not confirmed";
  return "not sent";
}

function amendLines(rec){
  const a = rec.amendment || {}, out = [];
  if (a.voided)
    out.push(["Voided", "This record does not count. " + a.voided.reason
      + " — voided " + when(a.voided.at)
      + (a.voided.by ? " by " + a.voided.by : "") + "."]);
  if (a.supersededBy)
    out.push(["Replaced", "A later record replaces this one: " + a.supersededBy + "."]);
  if (a.supersedes)
    out.push(["Replaces an earlier record", "This record replaces " + a.supersedes
      + (a.reason ? ": " + a.reason : "") + "."]);
  return out;
}

function recSheet(rec){
  const MARK = { done: ["d", "Cleared"], na: ["n", "N/A"], open: ["o", "Outstanding"] };
  let h = `<div class="wrap"><div class="rh">`
    + `<img src="data:image/png;base64,${LOGO}" alt="Parametrix">`
    + `<div><div class="rk">${esc(rec.form.document)} &middot; ${esc(rec.form.appendix)}</div>`
    + `<h1>${esc(rec.form.name)}</h1><div class="rk">Trimble MX60 Premium</div></div>`
    + `</div>`
    + amendLines(rec).map(l =>
        `<div class="amend"><b>${esc(l[0])}</b>${esc(l[1])}</div>`).join("")
    + `<table>`;
  const kv = (k, v) => { h += `<tr><th>${esc(k)}</th><td>${esc(v) || "&mdash;"}</td></tr>` };
  kv("Project", rec.job.project); kv("Task", rec.job.task);
  kv("Date", rec.job.date); kv("Operator", rec.job.operator);
  if (rec.job.vehicle) kv("Vehicle", rec.job.vehicle);
  for (const [k, v] of Object.entries(rec.meta)) if (v) kv(k.replace(/^\w/, c => c.toUpperCase()), v);
  kv("Record", rec.rid);
  kv("Completed", when(rec.completedAt) || "not complete");
  kv("Completed by", rec.signedBy);
  kv("Transfer", transferWords(rec.transfer));
  h += `</table>`;
  let group = null;
  for (const it of rec.items){
    if (it.group !== group){
      if (group !== null) h += `</table>`;
      h += `<h3>${esc(it.group)} &middot; ${esc(it.groupTitle)}</h3><table>`;
      group = it.group;
    }
    const [c, lbl] = MARK[it.state] || MARK.open;
    h += `<tr><td class="st ${c}">${lbl}</td><td>`
       + (it.n ? `<b>${esc(it.n)}.</b> ` : "") + esc(it.text)
       + (it.value ? `<span class="sn">${esc(it.valueLabel || "Value")}: ${esc(it.value)}</span>` : "")
       + (it.note ? `<span class="sn">${esc(it.note)}</span>` : "")
       + (it.sections.length ? `<span class="sn">${esc(it.sections.join(" · "))}</span>` : "")
       + `</td></tr>`;
  }
  if (group !== null) h += `</table>`;
  group = null;
  for (const f of rec.fields){
    if (f.group !== group){
      if (group !== null) h += `</table>`;
      h += `<h3>${esc(f.group)} &middot; ${esc(f.groupTitle)}</h3><table>`;
      group = f.group;
    }
    h += `<tr><th>${esc(f.label)}</th><td>${esc(f.text)
      || (f.required ? "<b>NOT RECORDED</b>" : "&mdash;")}</td></tr>`;
  }
  if (group !== null) h += `</table>`;
  for (const t of rec.tables){
    h += `<h3>${esc(t.group)} &middot; ${esc(t.groupTitle)}</h3><table>`
       + `<tr>${t.cols.map(c => `<th style="width:auto">${esc(c)}</th>`).join("")}</tr>`;
    for (const r of t.rows)
      h += `<tr>${r.map(c => `<td>${esc(c) || "&mdash;"}</td>`).join("")}</tr>`;
    h += `</table>`;
  }
  h += `<div class="sig"><div><b>Signed</b> ${esc(rec.signedBy) || "________________"}</div>`
     + `<div><b>Transfer</b> ${esc(transferWords(rec.transfer))}</div></div>`
     + `<div class="pf">${esc(rec.form.document)} ${esc(rec.form.appendix)}, Working `
     + `Version ${esc(rec.form.workingVersion)}, built from ${esc(rec.form.source)} `
     + `(${esc(rec.form.sourceHash)}). A living draft: nothing here is an adopted `
     + `Parametrix standard.</div></div>`;
  return h;
}
