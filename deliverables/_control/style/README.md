# Parametrix MX60 document style system

One visual system, four documents. Everything visual in the Technical Manual, the SOP, the Field
How To and the Office How To is specified here and nowhere else.

| File | What it is |
|---|---|
| `style-system.md` | **The specification.** Every named style, its rule, and where that rule comes from |
| `brand-tokens.css` | **The single source of values.** All four documents import it |
| `brand-source-status.md` | What the supplied Parametrix material establishes, and what is still awaiting the brand standard |

**Authority:** *Parametrix Brand Guide*, v6, November 2023, 32 pp.

## The rule that governs this directory

> **A style is either cited to a page of the brand guide, or it is marked as an extension.**
> There is no third category. Nothing in these files is a Parametrix brand rule unless the
> **Source** column gives its page.

An extension is a decision the guide does not make — monospace type, table styling, callout
styling, iconography, screen behaviour, a technical-report cover. Each is built from brand values
and each is listed in `brand-source-status.md` with the reason it exists. An extension is not a
proposal about what the Parametrix brand should be, and is not to be quoted as one.

**The company name is written in full.** The guide, p.5: do not abbreviate it. That applies to
document text, file names and code identifiers alike — which is why the tokens are `--brand-*`.
