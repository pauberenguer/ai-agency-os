# PDF Report Design Tokens

## Color System

| Token | Value | Usage |
|-------|-------|-------|
| `--primary` | `#1E3A5F` | Headers, borders, cover bg |
| `--primary-light` | `#2563EB` | Links, accents, client bars |
| `--primary-bg` | `#EFF6FF` | Info callout bg |
| `--accent` | `#0EA5E9` | Highlights |

## Score Colors

| Range | Color | Token | Hex |
|-------|-------|-------|-----|
| 80-100 | Dark Green | `--score-excellent` | `#059669` |
| 60-79 | Green | `--score-good` | `#10B981` |
| 40-59 | Orange | `--score-warning` | `#D97706` |
| 0-39 | Red | `--score-critical` | `#DC2626` |

## SVG Gauge Formula

```
Circle circumference = 2 × π × r = 2 × 3.14159 × 54 = 339.29

stroke-dasharray = "339.29"
stroke-dashoffset = 339.29 × (1 - score/100)

Examples:
  Score 100 → offset = 0
  Score 75  → offset = 84.82
  Score 50  → offset = 169.65
  Score 25  → offset = 254.47
  Score 0   → offset = 339.29
```

## Badge Classes

| Class | Background | Text | Use For |
|-------|-----------|------|---------|
| `badge-critical` | `#DC2626` | white | Critical severity |
| `badge-high` | `#D97706` | white | High severity |
| `badge-medium` | `#FBBF24` | `#78350F` | Medium severity |
| `badge-low` | `#10B981` | white | Low severity |
| `badge-pass` | `#059669` | white | Passing checks |
| `badge-effort` | `#2563EB` | white | Effort estimates |
| `badge-info` | `#6366F1` | white | Phase labels |

## Print Settings

- Page size: A4 (210mm × 297mm)
- Margins: 18mm top, 15mm sides, 22mm bottom
- Font: System sans-serif stack
- Base size: 10.5pt
- Line height: 1.6
- Max content width: 180mm
