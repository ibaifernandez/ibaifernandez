# **Emmet Abbreviations**

Emmet is a web-developer’s toolkit that can greatly improve your HTML & CSS workflow.

Basically, most text editors out there allow you to store and re-use commonly used code chunks, called “snippets”. While snippets are a good way to boost your productivity, all implementations have common pitfalls: you have to define the snippet first and you can’t extend them in runtime.

Emmet takes the snippets idea to a whole new level: you can type CSS-like expressions that can be dynamically parsed, and produce output depending on what you type in the abbreviation. Emmet is developed and optimised for web-developers whose workflow depends on HTML/XML and CSS, but can be used with programming languages too.

### Resources

-   [Emmet's Website](https://docs.emmet.io/abbreviations)

## What are Emmet Abbreviations?

Abbreviations are the heart of the Emmet toolkit: these special expressions are parsed in runtime and transformed into structured code block, HTML for example. The abbreviation’s syntax looks like CSS selectors with a few extensions specific to code generation. So every web-developer already knows how to use it.

**Example**

`#page>div.logo+ul#navigation>li*5>a{Item $}`

will yield

    <div id="page">
        <div class="logo"></div>
            <ul id="navigation">
            <li><a href="">Item 1</a></li>
            <li><a href="">Item 2</a></li>
            <li><a href="">Item 3</a></li>
            <li><a href="">Item 4</a></li>
            <li><a href="">Item 5</a></li>
        </ul>
    </div>

### Resources

-   [Emmet Abbreviations](https://docs.emmet.io/abbreviations)
