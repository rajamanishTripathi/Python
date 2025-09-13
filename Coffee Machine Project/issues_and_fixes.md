# Coffee Machine Project — Issues & Fixes Log

## 1. Function return placement
**Issue:** You asked why `return True` is outside the loop in `is_resource_sufficient`.

**Fix:** Putting `return True` after the loop ensures all items are checked. If it were inside an `else`, the function would return too early (after checking just the first ingredient).

---

## 2. Function call vs definition inside match
**Issue:** You wrote:
```python
case "espresso":
    def ww(start)
```
→ Pylance warned: `"start is not accessed"`

**Cause:** You accidentally used `def` instead of calling the function.

**Fix:** Should be:
```python
case "espresso":
    ww(start)
```

---

## 3. KeyError when checking cost
**Issue:** You wrote:
```python
if cost == MENU[start][cost]:
```
and got:
```
KeyError: 200
```

**Cause:** `cost` was being used as a dictionary key (e.g. `MENU['latte'][200]`) instead of checking `"cost"`.

**Fix:** Correct code:
```python
if cost == MENU[start]["cost"]:
```

---

## 4. String vs Integer mismatch
**Issue:** `input()` returns a string, but `MENU[start]["cost"]` is an integer.  
`"200" == 200 → always False.`

**Fix:** Convert input to integer:
```python
cost = int(input("How many rupees? "))
```

---

## 5. Wrong subtraction of resources
**Issue:** You wrote:
```python
resources[item] -= MENU[start]["ingredients"]
```
→ Tried subtracting a dictionary from an integer.

**Fix:** Subtract the correct ingredient value:
```python
resources[item] -= MENU[start]["ingredients"][item]
```

---

## 6. Report format
**Issue:** Resource report printed without formatting:
```python
for i,v in resources.items():
    print(i+": ",v)
```

**Fix (cleaner):**
```python
for item, amount in resources.items():
    print(f"{item}: {amount}")
```

---

## 7. Exact price requirement
**Current behavior:** User must enter exact rupees (e.g. 200 for latte).

**Improvement idea:** Allow overpayment and give change back instead of rejecting.
