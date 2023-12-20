import { SimilarProductsRenderer } from './SimilarProductsRenderer.js';
import { DefaultStyle } from './DefaultStyle.js';
import { renderSimilarProducts } from './RenderSimilarProducts.js';


// Creating an instance of SimilarProductsRenderer with DefaultStyle as the style parameter.
const defaultStyleRenderer = new SimilarProductsRenderer(new DefaultStyle());
// Calling the renderSimilarProducts function with the defaultStyleRenderer instance.
renderSimilarProducts(defaultStyleRenderer);
