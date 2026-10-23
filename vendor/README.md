# vendor

Third-party code committed here because the Field Tools app must work with no signal.

| | |
|---|---|
| `jspdf.umd.min.js` | jsPDF 2.5.2, UMD build, from the `jspdf` npm package. `tools/build-field-app.py` inlines it into the app, which is how a tablet in a vehicle writes a Parametrix PDF with nothing to fetch |

To update it: `npm install jspdf@<version>` then
`cp node_modules/jspdf/dist/jspdf.umd.min.js vendor/` and rebuild. Pin the version in
`package.json`; do not take a range.

Nothing else is vendored. The four documents and their pages have no runtime dependencies.
