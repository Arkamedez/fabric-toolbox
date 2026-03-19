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
| **Primary** | C&S Red | `#C8353D` | 1795 C | Logo, primary actions, headers, active states, alerts |
| **Secondary** | Corporate Gray | `#BFBFBF` | Cool Gray 9 C | Body text, secondary elements, axis labels, borders |
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
| 1 | Red | `#C8353D` | 1795 C | Default / first series |
| 2 | Dark Blue | `#1282C6` | 293 C | Second series, totals, secondary KPIs |
| 3 | Lime Green | `#79BE2E` | 382 C | Third series, positive indicators |
| 4 | Magenta | `#9F2C92` | 268 C | Fourth series, categorical contrast |
| 5 | Orange | `#E7703A` | 158 C | Fifth series, warnings |
| 6 | Light Blue | `#1E9FD3` | Process Blue C | Sixth series, informational |
| 7 | Dark Green | `#1C6B27` | 355 C | Seventh series, success states |
| 8 | Gray | `#BFBFBF` | Cool Gray 9 C | Eighth series, neutral/baseline |

### Semantic Colors

| Context | Color | Hex |
|---|---|---|
| ✅ Good / Positive | Dark Blue | `#1282C6` |
| ⚠️ Neutral / Info | Blue | `#1282C6` |
| ❌ Bad / Negative | Red | `#C8353D` |
| ▲ Increase (waterfall) | Dark Blue | `#1282C6` |
| ▼ Decrease (waterfall) | Red | `#C8353D` |
| ■ Total (waterfall) | Blue | `#1282C6` |

---

## 3. Typography

> [!IMPORTANT]
> **Arial** is the sole approved font family across all deliverables. Do not use specialty or decorative fonts. This ensures cross-platform consistency between Windows and macOS.

| Element | Font | Weight | Size | Color |
|---|---|---|---|---|
| **Page Title** | Arial | Bold | 16–20px | `#C8353D` |
| **Visual Title** | Arial | Bold | 12–14px | `#000000` |
| **Section Header** | Arial | Bold | 12px | `#1282C6` |
| **Body Text** | Arial | Regular | 10–11px | `#000000` |
| **Axis Labels** | Arial | Regular | 10px | `#BFBFBF` |
| **Data Labels** | Arial | Regular | 10px | `#BFBFBF` |
| **Table Headers** | Arial | Bold | 11px | `#FFFFFF` on `#C8353D` |
| **Table Values** | Arial | Regular | 10px | `#000000` |
| **Callout / KPI** | Arial | Bold | 28px | `#C8353D` |
| **Category Label** | Arial | Regular | 11px | `#BFBFBF` |
| **Legend** | Arial | Regular | 10px | `#BFBFBF` |
| **Tooltip** | Arial | Regular | 10px | `#000000` |

---

## 4. Component Specifications

### 4.1 Cards (KPI / Metric)

```
┌──────────────────────────┐
│  [Visual Title]          │  Arial Bold 12px #000000
│                          │
│       1,234              │  Arial Bold 28px #C8353D
│    Total Revenue         │  Arial Regular 11px #BFBFBF
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
│  Column A    │  Column B  │  Column C │  Header: #FFFFFF on #C8353D, Arial Bold 11px
├──────────────┼────────────┼───────────┤
│  Data Row 1  │  value     │  value    │  Row: #000000 on #FFFFFF, Arial 10px
│  Data Row 2  │  value     │  value    │  Alt Row: #000000 on #F2F2F2
│  Data Row 3  │  value     │  value    │
├──────────────┼────────────┼───────────┤
│  Total       │  value     │  value    │  Total: #FFFFFF on #1282C6, Arial Bold 11px
└──────────────┴────────────┴───────────┘
  Gridlines: #E6E6E6
  Outline: #BFBFBF
  Row Padding: 4px
```

### 4.3 Matrix (Pivot Table)

| Part | Font | Size | Foreground | Background |
|---|---|---|---|---|
| Column Headers | Arial Bold | 11px | `#FFFFFF` | `#C8353D` |
| Row Headers | Arial Bold | 11px | `#FFFFFF` | `#1282C6` |
| Values | Arial Regular | 10px | `#000000` | `#FFFFFF` |
| Subtotals | Arial Bold | 10px | `#000000` | `#F2F2F2` |
| Grand Total | Arial Bold | 11px | `#FFFFFF` | `#1282C6` |

### 4.4 Charts (Bar, Column, Line, Area)

| Element | Specification |
|---|---|
| Default bar/column fill | `#C8353D` (cycles through `dataColors` for multi-series) |
| Axis label color | `#BFBFBF` |
| Axis label font | Arial Regular 10px |
| Gridline color | `#E6E6E6` |
| Gridlines visible | Yes (value axis only) |
| Legend text | Arial Regular 10px, `#BFBFBF` |
| Data label text | Arial Regular 10px, `#BFBFBF` |
| Line stroke width | 2px |
| Background | `#FFFFFF` |

### 4.5 Slicers

| Element | Specification |
|---|---|
| Header text | Arial Bold 11px, `#C8353D` |
| Header outline | Bottom only |
| Item text | Arial Regular 11px, `#000000` |
| Outline color | `#C8353D`, weight 1px |
| Background | `#FFFFFF` |

### 4.6 Gauge

| Element | Specification |
|---|---|
| Fill arc | `#C8353D` |
| Target marker | `#BFBFBF` |
| Callout value | Arial Bold 20px, `#000000` |

### 4.7 Navigation & Buttons

| State | Background | Text | Border |
|---|---|---|---|
| **Primary** | `#C8353D` | `#FFFFFF` | none |
| **Primary Hover** | `#b01e24` | `#FFFFFF` | none |
| **Secondary** | `#FFFFFF` | `#C8353D` | 1px `#C8353D` |
| **Secondary Hover** | `#F2F2F2` | `#C8353D` | 1px `#C8353D` |
| **Disabled** | `#E6E6E6` | `#BFBFBF` | none |

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
- White text on Red (`#C8353D`) and Blue (`#1282C6`) backgrounds meets **WCAG AA** contrast (4.5:1+)
- Lime Green (`#79BE2E`) should only be used for filled shapes, **not** for text on white (fails contrast)
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
#C8353D  Red (Primary)     #C8353D  Series 1
#BFBFBF  Gray              #1282C6  Series 2
#000000  Black             #79BE2E  Series 3
#FFFFFF  White             #9F2C92  Series 4
                           #E7703A  Series 5
SURFACES                   #1E9FD3  Series 6
──────────                 #1C6B27  Series 7
#F2F2F2  Page BG           #BFBFBF  Series 8
#E6E6E6  Borders
#FFFFFF  Card BG           SEMANTIC
                           ────────
                           #1282C6  Good / Increase
                           #1282C6  Neutral / Total
                           #C8353D  Bad / Decrease
```
