# 7. Use DevTools (0.3 Marks)

## **Step 1: Open Chrome DevTools**

* **Windows:** `Ctrl + Shift + I`
* **Mac:** `Cmd + Option + I`
* **Shortcut to inspect a specific element:** `Ctrl + Shift + C` (Windows) / `Cmd + Shift + C` (Mac)

This opens the DevTools panel, usually docked to the side or bottom of Chrome.

---

## **Step 2: Inspect the page**

* In DevTools, go to the **Elements panel**.
* Here, you can see the full HTML structure of the page.
* Hidden inputs look like this in HTML:

```html
<input type="hidden" value="SECRET_VALUE_HERE">
```

---

## **Step 3: Use the Console to get the value**

* Switch to the **Console panel** (click “Console” at the top of DevTools).
* In the console, type the following command:

```javascript
document.querySelector('input[type="hidden"]').value
```

**Explanation:**

* `document` → represents the webpage.

* `querySelector('input[type="hidden"]')` → selects the first `<input>` element with `type="hidden"`.

* `.value` → retrieves the value of that input.

* Press **Enter**, and the hidden value will appear in the console.

---

## **Step 4: Copy the value**

* The console will display something like:

```
"mySecretValue123"
```

* This string is the **hidden input’s value**.

---
