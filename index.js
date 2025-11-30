// Create a simple html using JavaScript only

// Crete an html objects

// Call function to write content

let writeContent = (title_text, intro_text) => {
    
    //Write the page title
    document.title = title_text; // Set the title object

    // Error handle the the title
    if (document.title != title_text) {
        console.error("The title is incorrect")

    } else {
        console.log("The title is correct")
    };

    // Write intro to web page
    const para = document.createElement('p'); //Create a new element (Node)
    const node = document.createTextNode(intro_text); // Creates a text node
    para.appendChild(node); // Append the text node to <p> element
    document.body.appendChild(para) // Addend the <p> to body element

    console.log("Content create", Date());

};

let content = {
    title: "My web page generate with JavaScript",
    intro: "Welcome New User",
};

console.log("Write the content.");
/*
The DOMContentLoaded event fires when the HTML document has been completely parsed,
and all deferred scripts (<script defer src="…"> and <script type="module">) have downloaded and executed.
*/

document.addEventListener('DOMContentLoaded', () => {
    // Call the function
    writeContent(content.title, content.intro)
});





