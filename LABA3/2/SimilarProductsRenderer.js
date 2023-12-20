export class SimilarProductsRenderer {
    constructor(style) {
        this.style = style;
    }

    // Method to render the similar products in a specified 'container' using the provided 'data'.
    render(container, data) {
        // Clearing the existing content of the container before rendering new products.
        container.innerHTML = '';

        data.forEach(product => {
            // Creating a div element for each product and adding a CSS class.
            const productElement = document.createElement('div');
            productElement.classList.add('similar-product');

            // Creating an image element for the product with the source and alt attributes.
            const imgElement = document.createElement('img');
            imgElement.src = product.imageUrl;
            imgElement.alt = `Product ${product.id}`;

            // Adding a click event listener to navigate to the detailed product page on image click.
            imgElement.addEventListener('click', () => {
                window.location.href = `product_${product.id}.html`;
            });

            // Appending the image element to the product container and then to the main container.
            productElement.appendChild(imgElement);
            container.appendChild(productElement);
        });

        this.style.applyStyles(container);
    }
}
