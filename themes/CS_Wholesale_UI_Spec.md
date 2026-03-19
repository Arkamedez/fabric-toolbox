# C&S Wholesale Grocers — UI Design Specification

> **Version:** 1.0  
> **Date:** March 19, 2026  
> **Purpose:** Developer reference for building applications, dashboards, and reports aligned with the C&S Wholesale Grocers brand identity.

---

## 1. Corporate Color Palette

![Corporate Colors](C:/Users/jefft/.gemini/antigravity/brain/ae4be4da-b5d7-46fe-b240-cfe04cf01454/cs_corporate_colors_1773928605227.png)

These are the **primary brand colors** used for UI chrome, headers, navigation, logos, and body text.

| Role | Name | Hex | Pantone | Usage |
|---|---|---|---|---|
| **Primary** | C&S Red | `#d2232a` | 1795 C | Logo, primary actions, headers, active states, alerts |
| **Secondary** | Corporate Gray | `#58595b` | Cool Gray 9 C | Body text, secondary elements, axis labels, borders |
| **Text** | Black | `#000000` | — | Body copy, data values, maximum readability contexts |
| **Background** | White | `#FFFFFF` | — | Page backgrounds, card surfaces, clean space |

### Surface & Neutral Colors

| Name | Hex | Usage |
|---|---|---|
| Page Background | `#F2F2F2` | Canvas / outer page area behind cards |
| Card Surface | `#FFFFFF` | Visual container backgrounds |
| Divider / Grid | `#E6E6E6` | Table gridlines, borders, separators |
| Alternating Row | `#F2F2F2` | Banded table rows for readability |

---

## 2. Data Visualization Palette

![Data Palette](C:/Users/jefft/.gemini/antigravity/brain/ae4be4da-b5d7-46fe-b240-cfe04cf01454/cs_color_palette_1773928594642.png)

The **splash colors** are reserved for charts, graphs, and any visual requiring multiple distinct data series.

| Order | Name | Hex | Pantone | Primary Use |
|---|---|---|---|---|
| 1 | Red | `#d2232a` | 1795 C | Default / first series |
| 2 | Blue | `#005a9c` | 293 C | Second series, totals, secondary KPIs |
| 3 | Lime Green | `#c4d600` | 382 C | Third series, positive indicators |
| 4 | Purple | `#6a2a8d` | 268 C | Fourth series, categorical contrast |
| 5 | Orange | `#e87722` | 158 C | Fifth series, warnings |
| 6 | Cyan | `#00a9e0` | Process Blue C | Sixth series, informational |
| 7 | Dark Green | `#00843d` | 355 C | Seventh series, success states |
| 8 | Gray | `#58595b` | Cool Gray 9 C | Eighth series, neutral/baseline |

### Semantic Colors

| Context | Color | Hex |
|---|---|---|
| ✅ Good / Positive | Dark Green | `#00843d` |
| ⚠️ Neutral / Info | Blue | `#005a9c` |
| ❌ Bad / Negative | Red | `#d2232a` |
| ▲ Increase (waterfall) | Dark Green | `#00843d` |
| ▼ Decrease (waterfall) | Red | `#d2232a` |
| ■ Total (waterfall) | Blue | `#005a9c` |

---

## 3. Typography

> [!IMPORTANT]
> **Arial** is the sole approved font family across all deliverables. Do not use specialty or decorative fonts. This ensures cross-platform consistency between Windows and macOS.

| Element | Font | Weight | Size | Color |
|---|---|---|---|---|
| **Page Title** | Arial | Bold | 16–20px | `#d2232a` |
| **Visual Title** | Arial | Bold | 12–14px | `#000000` |
| **Section Header** | Arial | Bold | 12px | `#005a9c` |
| **Body Text** | Arial | Regular | 10–11px | `#000000` |
| **Axis Labels** | Arial | Regular | 10px | `#58595b` |
| **Data Labels** | Arial | Regular | 10px | `#58595b` |
| **Table Headers** | Arial | Bold | 11px | `#FFFFFF` on `#d2232a` |
| **Table Values** | Arial | Regular | 10px | `#000000` |
| **Callout / KPI** | Arial | Bold | 28px | `#d2232a` |
| **Category Label** | Arial | Regular | 11px | `#58595b` |
| **Legend** | Arial | Regular | 10px | `#58595b` |
| **Tooltip** | Arial | Regular | 10px | `#000000` |

---

## 4. Component Specifications

### 4.1 Cards (KPI / Metric)

```
┌──────────────────────────┐
│  [Visual Title]          │  Arial Bold 12px #000000
│                          │
│       1,234              │  Arial Bold 28px #d2232a
│    Total Revenue         │  Arial Regular 11px #58595b
│                          │
└──────────────────────────┘
  Background: #FFFFFF
  Border: 1px solid #E6E6E6
  Drop Shadow: subtle, #E6E6E6
  Padding: 8px
```

### 4.2 Tables

```
┌──────────────┬────────────┬───────────┐
│  Column A    │  Column B  │  Column C │  Header: #FFFFFF on #d2232a, Arial Bold 11px
├──────────────┼────────────┼───────────┤
│  Data Row 1  │  value     │  value    │  Row: #000000 on #FFFFFF, Arial 10px
│  Data Row 2  │  value     │  value    │  Alt Row: #000000 on #F2F2F2
│  Data Row 3  │  value     │  value    │
├──────────────┼────────────┼───────────┤
│  Total       │  value     │  value    │  Total: #FFFFFF on #005a9c, Arial Bold 11px
└──────────────┴────────────┴───────────┘
  Gridlines: #E6E6E6
  Outline: #58595b
  Row Padding: 4px
```

### 4.3 Matrix (Pivot Table)

| Part | Font | Size | Foreground | Background |
|---|---|---|---|---|
| Column Headers | Arial Bold | 11px | `#FFFFFF` | `#d2232a` |
| Row Headers | Arial Bold | 11px | `#FFFFFF` | `#005a9c` |
| Values | Arial Regular | 10px | `#000000` | `#FFFFFF` |
| Subtotals | Arial Bold | 10px | `#000000` | `#F2F2F2` |
| Grand Total | Arial Bold | 11px | `#FFFFFF` | `#005a9c` |

### 4.4 Charts (Bar, Column, Line, Area)

| Element | Specification |
|---|---|
| Default bar/column fill | `#d2232a` (cycles through `dataColors` for multi-series) |
| Axis label color | `#58595b` |
| Axis label font | Arial Regular 10px |
| Gridline color | `#E6E6E6` |
| Gridlines visible | Yes (value axis only) |
| Legend text | Arial Regular 10px, `#58595b` |
| Data label text | Arial Regular 10px, `#58595b` |
| Line stroke width | 2px |
| Background | `#FFFFFF` |

### 4.5 Slicers

| Element | Specification |
|---|---|
| Header text | Arial Bold 11px, `#d2232a` |
| Header outline | Bottom only |
| Item text | Arial Regular 11px, `#000000` |
| Outline color | `#d2232a`, weight 1px |
| Background | `#FFFFFF` |

### 4.6 Gauge

| Element | Specification |
|---|---|
| Fill arc | `#d2232a` |
| Target marker | `#58595b` |
| Callout value | Arial Bold 20px, `#000000` |

### 4.7 Navigation & Buttons

| State | Background | Text | Border |
|---|---|---|---|
| **Primary** | `#d2232a` | `#FFFFFF` | none |
| **Primary Hover** | `#b01e24` | `#FFFFFF` | none |
| **Secondary** | `#FFFFFF` | `#d2232a` | 1px `#d2232a` |
| **Secondary Hover** | `#F2F2F2` | `#d2232a` | 1px `#d2232a` |
| **Disabled** | `#E6E6E6` | `#58595b` | none |

---

## 5. Spacing & Layout

| Token | Value | Usage |
|---|---|---|
| `padding-card` | 8px | Inner padding for card visuals |
| `padding-page` | 16px | Page margin |
| `gap-visual` | 8px | Space between visuals |
| `border-radius` | 2–4px | Card corners |
| `border-weight` | 1px | Standard border thickness |
| `shadow` | `0 1px 3px #E6E6E6` | Card drop shadows |

---

## 6. Accessibility Notes

- All body text must be **Black** (`#000000`) on white backgrounds for maximum contrast
- White text on Red (`#d2232a`) and Blue (`#005a9c`) backgrounds meets **WCAG AA** contrast (4.5:1+)
- Lime Green (`#c4d600`) should only be used for filled shapes, **not** for text on white (fails contrast)
- Avoid using color alone to convey meaning — always pair with labels or icons
- Minimum font size: **10px** for any readable text

---

## 7. Power BI Theme File

The companion Power BI theme JSON implementing this spec is available at:

**[CS_Wholesale_Theme.json](file:///C:/GIT/FUAM/themes/CS_Wholesale_Theme.json)**

**To apply:** Power BI Desktop → View → Themes → Browse for themes → select `CS_Wholesale_Theme.json`

---

## 8. Quick Reference — Color Codes

```
CORPORATE                  SPLASH / DATA SERIES
─────────────              ──────────────────────
#d2232a  Red (Primary)     #d2232a  Series 1
#58595b  Gray              #005a9c  Series 2
#000000  Black             #c4d600  Series 3
#FFFFFF  White             #6a2a8d  Series 4
                           #e87722  Series 5
SURFACES                   #00a9e0  Series 6
──────────                 #00843d  Series 7
#F2F2F2  Page BG           #58595b  Series 8
#E6E6E6  Borders
#FFFFFF  Card BG           SEMANTIC
                           ────────
                           #00843d  Good / Increase
                           #005a9c  Neutral / Total
                           #d2232a  Bad / Decrease
```
