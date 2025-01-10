import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.write(
    """# When does π = 4?
*Can π be other values than 3.14?* Yes it can, it can actually take on other values depending on the geometry.
For example, in non-euclidean geometry it can take on other values. 

We're concerned with when π=4, so when does this happen? Well π represents the ratio of circumfrence to diameter but in the 
normal 2D geometry we're used to this doesn't apply when we change the value of π because π is a constant, meaning it doesn't change.
However, in another geometry with different rules it will change.

In euclidean geometry distance is defined by the square root of squared differences.

$$\\text{distance}=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

However, in taxicab geometry, distance is defined by the absolute value of differences.

$$\\text{distance}=|x_2-x_1|+|y_2-y_1|$$

This means distance is defined on a square grid rather than absolutely. I can plot the distance between two points by drawing straight lines only."""
)

# Replace with your own GIF file path or URL
gif_url = "graphics.gif"

st.image(gif_url, caption="Euclidean vs. Taxicab", use_column_width=True)

st.write(
    """
A circle is defined as a shape on which every point is equidistant from the center. In taxicab geometry this takes the shape of a diamond with radius *r*.

$$|x|+|y|=r$$

This shape has four sides and so the perimeter of the shape is four times the diameter.
The diameter is just two times the radius so if we divide the perimeter by two times the radius we get 4.

$$π_1=\\frac{C}{2\\cdot r}=\\frac{2 \\cdot 4 \\cdot r}{2 \\cdot r} = 4$$

π can be 4 when we use taxicab geometry. In fact, this is the same geometry of the game Tetris, so when you play Tetris you're really playing in
a geometry where π = 4. Imagine living in Tetris forever. Traversing a circle in Tetris would mean you travel four times the diameter rather than 3.14 times the diameter."""
)

st.write(
    """Try it yourself! In the sidebar to the left enter a radius and watch as the diamond expands. See how the perimeter changes but not the value of π."""
)


r = st.sidebar.slider("Select a value for r", 0.1, 10.0)


st.sidebar.write(f"**r = {r}**")


perimeter = 4 * 2 * r

st.sidebar.write(f"**C = {perimeter}**")

pi = perimeter / (2 * r)

st.sidebar.write(f"**π = {pi}**")
print(f"|x|+|y|={r}")

# 2. Create an HTML block that loads Desmos and sets an expression
desmos_html = f"""
<!DOCTYPE html>
<html>
  <head>
    <!-- Load Desmos from CDN -->
    <script src="https://www.desmos.com/api/v1.0/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
  </head>
  <body>
    <!-- The element that will host the Desmos calculator -->
    <div id="calculator" style="width: 600px; height: 400px;"></div>

    <script>
      // 1. Create the calculator
      var elt = document.getElementById('calculator');
      var calculator = Desmos.GraphingCalculator(elt, {{
        expressions: true,
        keypad: true
      }});

      // 2. Plot the diamond equation with the current radius
      //    e.g., |x| + |y| = 3
      calculator.setExpression({{ 
        id: 'diamond', 
        latex: 'abs(x) + abs(y) = {r}' 
      }});

      // Optionally: adjust the viewport so the diamond is visible
      calculator.setMathBounds({{
        left: -{r}*1.5,
        right: {r}*1.5,
        bottom: -{r}*1.5,
        top: {r}*1.5
      }});
    </script>
  </body>
</html>
"""

# 3. Render the HTML in Streamlit using components.html
#    Increase height if you want more vertical space
components.html(desmos_html, height=450)
