// Sample Product Data
const products = [
    {
      id: 1,
      name: "Smartphone",
      price: 699.99,
      image: "https://via.placeholder.com/200",
    },
    {
      id: 2,
      name: "Laptop",
      price: 1299.99,
      image: "https://via.placeholder.com/200",
    },
    {
      id: 3,
      name: "Headphones",
      price: 199.99,
      image: "https://via.placeholder.com/200",
    },
    {
      id: 4,
      name: "Smartwatch",
      price: 299.99,
      image: "https://via.placeholder.com/200",
    },
  ];
  
  // Initialize Cart
  let cartCount = 0;
  
  // Dynamically Render Products
  const productsContainer = document.getElementById("products");
  
  products.forEach((product) => {
    const productCard = document.createElement("div");
    productCard.classList.add("product-card");
    
    productCard.innerHTML = `
      <img src="${product.image}" alt="${product.name}">
      <h2>${product.name}</h2>
      <p>$${product.price.toFixed(2)}</p>
      <button onclick="addToCart()">Add to Cart</button>
    `;
  
    productsContainer.appendChild(productCard);
  });
  
  // Handle Add to Cart
  function addToCart() {
    cartCount++;
    document.getElementById("cart-count").textContent = cartCount;
  }
  