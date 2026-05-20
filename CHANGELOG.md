# Changelog

## v0.1.0 (2026-05-21)

- Initial release
- 9 repair stages: markdown stripping, comment stripping, BOM stripping, quote fixing, literal fixing, comma fixing, value fixing, control char escaping, bracket auto-close
- Code extraction from fenced, indented, inline, and XML blocks
- JSON block extraction from surrounding text
- Rich result object with repair metadata
- CLI tool for file/stdin repair and code extraction
