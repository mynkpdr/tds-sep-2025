# 12. CSS: Featured-Sale Discount Sum (0.4 Marks)

Objective
---------

Use your browser's DevTools to identify elements with both a `featured` and a `sale` class, and then sum the values of their `data-discount` attributes.

Steps to Get the Answer
-----------------------

### Method 1: Using the DevTools Console (Recommended)

1. **Open Developer Tools:**

    - On the quiz page, right-click near the question and select "Inspect".

2. **Go to the Console:**

    - Click on the "Console" tab in the DevTools window.

3. **Run the JavaScript Snippet:**

    - The CSS selector to find elements that have *both* classes is `.featured.sale`.

    - Paste the following JavaScript code into the console and press `Enter`. This code selects all matching elements, extracts the `data-discount` value from each, converts it to a number, and calculates the sum.

    ```javascript
    let totalDiscount = 0;
    document.querySelectorAll('.featured.sale').forEach(item => {
        totalDiscount += parseInt(item.getAttribute('data-discount'), 10);
    });
    console.log(totalDiscount);

    ```

4. **Get the Result:**

    - The console will print the final sum.

5. **Submit the Answer:**

    - Enter this number into the answer box.

### Method 2: Manual Inspection

1. **Open Developer Tools** and go to the "Elements" panel.

2. Locate the `<ul class="products d-none">` list in the HTML.

3. Manually look through each `<li>` element.

4. If an element has both `featured` and `sale` in its `class` attribute (e.g., `<li class="featured sale vip" ...>`), find its `data-discount` value.

5. Add up the discount values for all matching elements.
