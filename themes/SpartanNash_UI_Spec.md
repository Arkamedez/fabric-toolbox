# SpartanNash - UI Design Specification

> **Version:** 1.2  
> **Date:** March 20, 2026  
> **Purpose:** Developer reference for building applications, dashboards, and reports aligned with the SpartanNash brand identity.

---

## 1. Corporate Color Palette

These are the **primary brand colors** used for UI chrome, headers, navigation, logos, and body text.

| Role | Name | Hex | Usage |
|---|---|---|---|
| **Primary** | SPTN Dark Green | `#006A52` | Visual headers, primary titles, navigation |
| **Secondary** | SPTN Mid Green | `#43B02A` | Section headers, primary actions |
| **Tertiary** | SPTN Light Green | `#A4D65E` | Secondary elements, positive indicators |
| **Background** | White | `#FFFFFF` | Page backgrounds, card surfaces |
| **Neutral** | Dark Gray | `#525051` | Labels, axis text, informational text |

### 1.1 Surface & Neutral Colors

| Name | Hex | Usage |
|---|---|---|
| Page Background | `#F2F2F2` | Canvas / outer page area behind cards |
| Card Surface | `#FFFFFF` | Visual container backgrounds |
| Divider / Grid | `#CCE1DC` | Table gridlines, borders, separators |
| Alternating Row | `#E4E4E5` | Banded table rows for readability |

---

## 2. Data Visualization Palette

The **splash colors** are reserved for charts, graphs, and any visual requiring multiple distinct data series.

| Order | Name | Hex | Primary Use |
|---|---|---|---|
| 1 | Dark Green | `#006A52` | Default / first series |
| 2 | Mid Green | `#43B02A` | Second series |
| 3 | Light Green | `#A4D65E` | Third series |
| 4 | Gold | `#FFC72C` | Fourth series |
| 5 | Teal Gray | `#99C3BA` | Fifth series |
| 6 | Sage Green | `#8ED07F` | Sixth series |
| 7 | Pale Green | `#C8E69E` | Seventh series |
| 8 | Pale Gold | `#FFDD80` | Eighth series |
| 9-14 | Extended Palette | Varied | See Section 8 for samples |

### 2.1 Semantic Colors & Conditional Formatting

| Context | Color | Hex | Usage Notes |
|---|---|---|---|
| ✅ Good / Positive | Light Green | `#A4D65E` | KPIs hitting target, success states. |
| ⚠️ Neutral / Info | Blue | `#3D7AA9` | Informational callouts. |
| ❌ Bad / Negative | Red | `#EB1316` | Missing targets, errors. |
| ▲ Increase (waterfall) | Light Green | `#A4D65E` | Positive flow. |
| ▼ Decrease (waterfall) | Red | `#EB1316` | Negative flow. |
| ■ Total (waterfall) | Dark Green | `#006A52` | Neutral aggregation. |

---

## 3. Typography

> [!IMPORTANT]
> **Arial** is the approved font family across all deliverables.

| Element | Font | Weight | Size | Color |
|---|---|---|---|---|
| **Page Title** | Arial | Bold | 16–20px | `#006A52` |
| **Visual Title** | Arial | Bold | 11px | `#006A52` |
| **Section Header** | Arial | Bold | 10.5px | `#43B02A` |
| **Body Text** | Arial | Regular | 10px | `#000000` |
| **Axis Labels** | Arial | Regular | 10px | `#525051` |
| **Data Labels** | Arial | Regular | 10px | `#525051` |
| **Table Headers** | Arial | Bold | 10px | `#000000` on `#FFFFFF` |
| **Table Values** | Arial | Regular | 10px | `#000000` |
| **Callout / KPI** | Arial | Bold | 16px | `#000000` |
| **Category Label** | Arial | Regular | 10px | `#525051` |
| **Legend** | Arial | Regular | 10px | `#525051` |
| **Tooltip** | Arial | Regular | 10px | `#000000` |

---

## 4. Component Specifications

### 4.1 Cards (KPI / Metric)

```
┌──────────────────────────┐
│  [Visual Title]          │  Arial Bold 11px #006A52
│                          │
│       1,234              │  Arial Bold 16px #000000
│    Category Label        │  Arial Regular 10px #525051
│                          │
└──────────────────────────┘
  Background: #FFFFFF
  Border: Solid #A1A1A1, weight 1px
  Border Radius: 16px
  Padding: 8px
```

### 4.2 Tables

```
┌──────────────┬────────────┬───────────┐
│  Column A    │  Column B  │  Column C │  Header: #000000 on #FFFFFF, Arial Bold 10px
|              |            |           |  Outline: Bottom Only #A1A1A1
├──────────────┼────────────┼───────────┤
│  Data Row 1  │  value     │  value    │  Row: Arial 10px, #000000, Background #FFFFFF
│  Data Row 2  │  value     │  value    │  Alt Row: Background #E4E4E5
└──────────────┴────────────┴───────────┘
```

### 4.3 Matrix (Pivot Table)

| Part | Font | Size | Foreground | Background |
|---|---|---|---|---|
| Column Headers | Arial Bold | 10px | `#000000` | `#FFFFFF` |
| Row Headers | Arial Bold | 10px | `#000000` | `#FFFFFF` |
| Values | Arial Regular | 10px | `#000000` | `#FFFFFF` |
| Subtotals | Arial Bold | 10px | `#000000` | `#E4E4E5` |
| Grand Total | Arial Bold | 10px | `#000000` | `#A4D65E` |

### 4.4 Charts (Bar, Column, Line, Area)

| Element | Specification |
|---|---|
| Default bar/column fill | `#006A52` |
| Axis label color | `#525051` |
| Axis label font | Arial Regular 10px |
| Gridline color | `#CCE1DC` |
| Gridlines visible | Yes (value axis only) |
| Legend text | Arial Regular 10px, `#525051` |
| Data label text | Arial Regular 10px, `#525051` |
| Line stroke width | 2px |
| Background | `#FFFFFF` |

### 4.5 Slicers

| Element | Specification |
|---|---|
| Header text | Arial Bold 11px, `#006A52` |
| Item text | Arial Regular 10px, `#000000` |
| Background | `#FFFFFF` |

### 4.6 Gauge

| Element | Specification |
|---|---|
| Fill arc | `#006A52` |
| Target marker | `#525051` |
| Callout value | Arial Bold 16px, `#000000` |

### 4.7 Navigation & Buttons

| State | Background | Text | Border |
|---|---|---|---|
| **Primary** | `#006A52` | `#FFFFFF` | none |
| **Primary Hover** | `#43B02A` | `#FFFFFF` | none |
| **Secondary** | `#FFFFFF` | `#006A52` | 1px `#006A52` |
| **Secondary Hover** | `#E4E4E5` | `#006A52` | 1px `#006A52` |

---

## 5. Spacing & Layout

| Token | Value | Usage |
|---|---|---|
| `padding-card` | 8px | Inner padding for card visuals |
| `padding-page` | 16px | Page margin |
| `gap-visual` | 8px | Space between visuals |
| `border-radius` | 16px | Globally applied to visual borders |
| `border-weight` | 1px | Applied to visual containers |
| `shadow` | `0 2px 4px #A1A1A1` | (Optional) Subtle card drop shadows |

---

## 6. Accessibility Notes
- All body text must be **Black** (`#000000`) on white backgrounds for maximum contrast
- Avoid using color alone to convey meaning — always pair with labels or icons
- Minimum font size: **10px** for any readable text
- Secondary series colors (Yellow/Gold) should only be used for filled shapes, **not** for text on white
- Use distinct icons (▲ ▼) for variance metrics to support color-blind users

---

## 7. Power BI Theme File
The companion Power BI theme JSON for SpartanNash is available at:
**[SpartanNash Theme.json](file:///C:/GIT/FUAM/themes/SpartanNash%20Theme.json)**

---

## 8. Quick Reference - Color Codes

| Category | Role / Element | Hex | Sample |
|---|---|---|---|
| **Corporate** | SPTN Dark Green | `#006A52` | ![#006A52](https://placehold.co/15x15/006A52/006A52.png) |
| | SPTN Mid Green | `#43B02A` | ![#43B02A](https://placehold.co/15x15/43B02A/43B02A.png) |
| | SPTN Light Green | `#A4D65E` | ![#A4D65E](https://placehold.co/15x15/A4D65E/A4D65E.png) |
| | SPTN Neutral | `#525051` | ![#525051](https://placehold.co/15x15/525051/525051.png) |
| **Surfaces** | Divider / Grid | `#CCE1DC` | ![#CCE1DC](https://placehold.co/15x15/CCE1DC/CCE1DC.png) |
| | Alternating Row | `#E4E4E5` | ![#E4E4E5](https://placehold.co/15x15/E4E4E5/E4E4E5.png) |
| **Semantic** | Good / Positive | `#A4D65E` | ![#A4D65E](https://placehold.co/15x15/A4D65E/A4D65E.png) |
| | Neutral / Info | `#3D7AA9` | ![#3D7AA9](https://placehold.co/15x15/3D7AA9/3D7AA9.png) |
| | Bad / Negative | `#EB1316` | ![#EB1316](https://placehold.co/15x15/EB1316/EB1316.png) |
| **Scale** | Maximum (Good) | `#700017` | ![#700017](https://placehold.co/15x15/700017/700017.png) |
| | Center (Neutral)| `#ED6102` | ![#ED6102](https://placehold.co/15x15/ED6102/ED6102.png) |
| | Minimum (Bad) | `#FFBE0E` | ![#FFBE0E](https://placehold.co/15x15/FFBE0E/FFBE0E.png) |

---

## Document History
* **v1.2** (March 20, 2026): Added 1.1 Surface section and expanded Section 3 Typography for 100% parity with C&S detail levels.
* **v1.1** (March 20, 2026): Added extended color palette colors and button specifications.
* **v1.0** (March 20, 2026): Initial UI design specification migration.
