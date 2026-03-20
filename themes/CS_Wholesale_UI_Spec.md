# C&S Wholesale Grocers - UI Design Specification

> **Version:** 1.1  
> **Date:** March 20, 2026  
> **Purpose:** Developer reference for building applications, dashboards, and reports aligned with the C&S Wholesale Grocers brand identity.

---

## 1. Corporate Color Palette

![Corporate Colors](C:/Users/jefft/.gemini/antigravity/brain/ae4be4da-b5d7-46fe-b240-cfe04cf01454/cs_corporate_colors_1773928605227.png)

These are the **primary brand colors** used for UI chrome, headers, navigation, logos, and body text.

| Role | Name | Hex | Usage |
|------|------|------|------|
| **Primary** | C&S Red | `#C8353D` | Logo, primary actions, headers, active states, alerts |
| **Secondary** | Corporate Gray | `#BFBFBF` | Body text, secondary elements, axis labels, borders |
| **Text** | Black | `#000000` | Body copy, data values, maximum readability contexts |
| **Background** | White | `#FFFFFF` | Page backgrounds, card surfaces, clean space |

### Surface & Neutral Colors

| Name | Hex | Usage |
|------|------|------|
| Page Background | `#F2F2F2` | Canvas / outer page area behind cards |
| Card Surface | `#FFFFFF` | Visual container backgrounds |
| Divider / Grid | `#E6E6E6` | Table gridlines, borders, separators |
| Alternating Row | `#F2F2F2` | Banded table rows for readability |

---

## 2. Data Visualization Palette

![Data Palette](C:/Users/jefft/.gemini/antigravity/brain/ae4be4da-b5d7-46fe-b240-cfe04cf01454/cs_color_palette_1773928594642.png)

The **splash colors** are reserved for charts, graphs, and any visual requiring multiple distinct data series.

| Order | Name | Hex | Primary Use |
|------|------|------|------|
| 1 | Red | `#C8353D` | Default / first series |
| 2 | Dark Blue | `#1282C6` | Second series, totals, secondary KPIs |
| 3 | Lime Green | `#79BE2E` | Third series, positive indicators |
| 4 | Magenta | `#9F2C92` | Fourth series, categorical contrast |
| 5 | Orange | `#E7703A` | Fifth series, warnings |
| 6 | Light Blue | `#1E9FD3` | Sixth series, informational |
| 7 | Dark Green | `#1C6B27` | Seventh series, success states |
| 8 | Gray | `#BFBFBF` | Eighth series, neutral/baseline |

### Semantic Colors & Conditional Formatting

| Context | Color | Hex | Usage Notes |
|------|------|------|------|
| ✅ Good / Positive | Dark Green | `#1C6B27` | KPIs hitting target, success states, positive variance. Safe for text on white. |
| ⚠️ Neutral / Info | Gray | `#BFBFBF` | Informational callouts, baseline metrics, unchanged values. |
| ❌ Bad / Negative | Red | `#C8353D` | Missing targets, errors, negative variance, critical alerts. |
| ▲ Increase (waterfall) | Dark Green | `#1C6B27` | Positive flow. |
| ▼ Decrease (waterfall) | Red | `#C8353D` | Negative flow. |
| ■ Total (waterfall) | Dark Blue | `#1282C6` | Neutral aggregation. |

#### Conditional Formatting Guidelines
* **Do not use Lime Green (`#79BE2E`) for text**. Use **Dark Green (`#1C6B27`)** to maintain WCAG text contrast on white backgrounds. Lime Green is reserved for filled shapes only.
* **Diverging/Gradient Scales:** When using background color conditionally on a continuous metric (e.g., heatmaps or matrix backgrounds), use the following 3-color scale:
  * Minimum / Bad: **Red (`#C8353D`)**
  * Center / Neutral: **White (`#FFFFFF`)**
  * Maximum / Good: **Dark Green (`#1C6B27`)**

---

## 3. Typography

> [!IMPORTANT]
> **Arial** is the sole approved font family across all deliverables. Do not use specialty or decorative fonts. This ensures cross-platform consistency between Windows and macOS.

| Element | Font | Weight | Size | Color |
|------|------|------|------|------|
| **Page Title** | Arial | Bold | 16–20px | `#C8353D` |
| **Visual Title** | Arial | Bold | 12–14px | `#1282C6` |
| **Section Header** | Arial | Bold | 12px | `#1282C6` |
| **Body Text** | Arial | Regular | 10–11px | `#000000` |
| **Axis Labels** | Arial | Regular | 10px | `#BFBFBF` |
| **Data Labels** | Arial | Regular | 10px | `#BFBFBF` |
| **Table Headers** | Arial | Bold | 11px | `#FFFFFF` on `#1282C6` |
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
│  [Visual Title]          │  Arial Bold 12px #1282C6
│                          │
│       1,234              │  Arial Bold 28px #C8353D
│    Total Revenue         │  Arial Regular 11px #BFBFBF
│                          │
└──────────────────────────┘
  Background: #F2F2F2
  Border: none
  Drop Shadow: subtle, #E6E6E6
  Padding: 8px
```

### 4.2 Tables

```
┌──────────────┬────────────┬───────────┐
│  Column A    │  Column B  │  Column C │  Header: #FFFFFF on #1282C6, Arial Bold 11px
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
|------|------|------|------|------|
| Column Headers | Arial Bold | 11px | `#FFFFFF` | `#1282C6` |
| Row Headers | Arial Bold | 11px | `#FFFFFF` | `#1282C6` |
| Values | Arial Regular | 10px | `#000000` | `#FFFFFF` |
| Subtotals | Arial Bold | 10px | `#000000` | `#F2F2F2` |
| Grand Total | Arial Bold | 11px | `#FFFFFF` | `#1282C6` |

### 4.4 Charts (Bar, Column, Line, Area)

| Element | Specification |
|------|------|
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
|------|------|
| Header text | Arial Bold 11px, `#1282C6` |
| Header outline | Bottom only |
| Item text | Arial Regular 11px, `#000000` |
| Outline color | `#1282C6`, weight 1px |
| Background | `#FFFFFF` |

### 4.6 Gauge

| Element | Specification |
|------|------|
| Fill arc | `#C8353D` |
| Target marker | `#BFBFBF` |
| Callout value | Arial Bold 20px, `#000000` |

### 4.7 Navigation & Buttons

| State | Background | Text | Border |
|------|------|------|------|
| **Primary** | `#C8353D` | `#FFFFFF` | none |
| **Primary Hover** | `#b01e24` | `#FFFFFF` | none |
| **Secondary** | `#FFFFFF` | `#C8353D` | 1px `#C8353D` |
| **Secondary Hover** | `#F2F2F2` | `#C8353D` | 1px `#C8353D` |
| **Disabled** | `#E6E6E6` | `#BFBFBF` | none |

---

## 5. Spacing & Layout

| Token | Value | Usage |
|------|------|------|
| `padding-card` | 8px | Inner padding for card visuals |
| `padding-page` | 16px | Page margin |
| `gap-visual` | 8px | Space between visuals |
| `border-radius` | 2–4px | Card corners |
| `border-weight` | none | Borders disabled globally |
| `shadow` | `0 1px 3px #E6E6E6` | Card drop shadows |

---

## 6. Accessibility Notes

- All body text must be **Black** (`#000000`) on white backgrounds for maximum contrast
- White text on Red (`#C8353D`) and Blue (`#1282C6`) backgrounds meets **WCAG AA** contrast (4.5:1+)
- Lime Green (`#79BE2E`) should only be used for filled shapes, **not** for text on white (fails contrast)
- Avoid using color alone to convey meaning - always pair with labels or icons
- Minimum font size: **10px** for any readable text

---

## 7. Power BI Theme File

The companion Power BI theme JSON implementing this spec is available at:

**[CS_Wholesale_Theme.json](file:///C:/GIT/FUAM/themes/CS_Wholesale_Theme.json)**

**To apply:** Power BI Desktop → View → Themes → Browse for themes → select `CS_Wholesale_Theme.json`

---

## 8. Quick Reference - Color Codes

| Category | Role / Element | Hex | Sample |
|---|---|---|---|
| **Corporate** | Red (Primary) | `#C8353D` | ![#C8353D](https://placehold.co/15x15/C8353D/C8353D.png) |
| | Gray | `#BFBFBF` | ![#BFBFBF](https://placehold.co/15x15/BFBFBF/BFBFBF.png) |
| | Black | `#000000` | ![#000000](https://placehold.co/15x15/000000/000000.png) |
| | White | `#FFFFFF` | ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) |
| **Surfaces** | Page BG | `#F2F2F2` | ![#F2F2F2](https://placehold.co/15x15/F2F2F2/F2F2F2.png) |
| | Borders | `#E6E6E6` | ![#E6E6E6](https://placehold.co/15x15/E6E6E6/E6E6E6.png) |
| | Card BG | `#FFFFFF` | ![#FFFFFF](https://placehold.co/15x15/FFFFFF/FFFFFF.png) |
| **Splash Series**| Series 1 | `#C8353D` | ![#C8353D](https://placehold.co/15x15/C8353D/C8353D.png) |
| | Series 2 | `#1282C6` | ![#1282C6](https://placehold.co/15x15/1282C6/1282C6.png) |
| | Series 3 | `#79BE2E` | ![#79BE2E](https://placehold.co/15x15/79BE2E/79BE2E.png) |
| | Series 4 | `#9F2C92` | ![#9F2C92](https://placehold.co/15x15/9F2C92/9F2C92.png) |
| | Series 5 | `#E7703A` | ![#E7703A](https://placehold.co/15x15/E7703A/E7703A.png) |
| | Series 6 | `#1E9FD3` | ![#1E9FD3](https://placehold.co/15x15/1E9FD3/1E9FD3.png) |
| | Series 7 | `#1C6B27` | ![#1C6B27](https://placehold.co/15x15/1C6B27/1C6B27.png) |
| | Series 8 | `#BFBFBF` | ![#BFBFBF](https://placehold.co/15x15/BFBFBF/BFBFBF.png) |
| **Semantic** | Good / Increase | `#1C6B27` | ![#1C6B27](https://placehold.co/15x15/1C6B27/1C6B27.png) |
| | Neutral | `#BFBFBF` | ![#BFBFBF](https://placehold.co/15x15/BFBFBF/BFBFBF.png) |
| | Total | `#1282C6` | ![#1282C6](https://placehold.co/15x15/1282C6/1282C6.png) |
| | Bad / Decrease | `#C8353D` | ![#C8353D](https://placehold.co/15x15/C8353D/C8353D.png) |

---

## Document History
* **v1.1** (March 20, 2026): Expanded semantic colors and conditional formatting guidelines; corrected Good/Neutral indicators.
* **v1.0** (March 19, 2026): Initial UI design specification.
