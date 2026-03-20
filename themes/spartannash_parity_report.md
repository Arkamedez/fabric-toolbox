# SpartanNash Parity Report: Theme JSON vs. UI Spec (v1.2)

This report details the discrepancies between the newly finalized `SpartanNash_UI_Spec.md` and the existing `SpartanNash Theme.json` file. 

The current JSON file is very sparse and requires significant updates to reach parity with the detailed UI Spec.

## 1. Global & Structural Discrepancies

| Element | Status | In UI Spec (MD) | In Theme JSON |
|---|---|---|---|
| **Data Colors (`dataColors`)** | ❌ Mismatch | 14 values (including extended palette) | Only 8 values |
| **Global Background** | ❌ Missing in JSON | `#FFFFFF` | Not defined |
| **Global Borders** | ❌ Missing in JSON | 1px Solid `#A1A1A1`, Radius 16px | Not defined |
| **Global Shadows** | ❌ Missing in JSON | `0 2px 4px #A1A1A1` | Not defined |
| **Page Outspace** | ✅ Aligned | `#F2F2F2` (Page Background) | `#F2F2F2` |
| **Semantic Colors**| ✅ Aligned | `Good: #A4D65E`, `Neutral: #3D7AA9`, `Bad: #EB1316` | Defined precisely |

## 2. Typography Discrepancies (`textClasses`)

| Element | Status | In UI Spec (MD) | In Theme JSON |
|---|---|---|---|
| **Callout / KPI** | ❌ Mismatch | Arial, **Bold, 16px, `#000000`** | Arial, **10px, No Color Set** |
| **Visual Title** | ❌ Mismatch | Arial, Bold, **11px**, `#006A52` | Arial, **10px**, `#006A52` |
| **Section Header** | ❌ Mismatch | Arial, Bold, **10.5px**, `#43B02A` | Arial, **No Size Set**, `#43B02A` |
| **Label** | ✅ Aligned | Arial, `#525051` | Arial, `#525051` |

## 3. Component Discrepancies (`visualStyles`) 
*Most components defined in the new spec are completely missing from the existing JSON.*

| Component | Status | Missing from JSON |
|---|---|---|
| **Cards (`card`)** | ❌ Missing | Missing background (`#FFFFFF`), borders (`#A1A1A1`, radius 16px), and accurate callout styling. |
| **Tables (`tableEx`)** | ❌ Missing | Missing gridline colors (`#CCE1DC`), outline (`#A1A1A1`), header styles (`#000000` on white), and alternating rows (`#E4E4E5`). |
| **Matrix (`pivotTable`)** | ❌ Missing | Missing Subtotal backgrounds (`#E4E4E5`) and Grand Total backgrounds (`#A4D65E`). |
| **Charts (Bar/Line/Area)** | ❌ Missing | Missing gridline styles (`#CCE1DC`), line stroke width (2px), and axis label colors (`#525051`). |
| **Slicers (`slicer`)** | ❌ Missing | Missing header color (`#006A52`, 11px) and background (`#FFFFFF`). |
| **Gauge (`gauge`)** | ❌ Missing | Missing fill arc (`#006A52`) and target marker (`#525051`). |
| **Waterfall Sentiment** | ❌ Missing | Missing explicit increase (`#A4D65E`), decrease (`#EB1316`), and total (`#006A52`) fill definitions within the `waterfallChart` section. |

## 4. Present in JSON, Missing in Spec
- **`outspacePane > checkboxAndApplyColor: #FFC72C`**: The JSON defines a specific yellow color for checkboxes in the filter pane. This is a very specific Power BI Desktop detail not normally listed in a UI spec, but it is acceptable to exist.

## Recommended Next Steps
To synchronize these files, the `SpartanNash Theme.json` must be heavily expanded. We need to:
1. Update `textClasses` to match font sizes precisely.
2. Insert global `*` > `*` styles for backgrounds, borders, and shadows.
3. Add specific component definitions (`tableEx`, `pivotTable`, `card`, `slicer`, `gauge`, `waterfallChart`) matching the C&S structure but using SpartanNash hex colors.
