// --- 1. Data Structures ---
// Array of objects representing our menu with emojis
const menu = [
  { id: "m1", name: "Nebula Nectar", price: 4.5, icon: "🌌" },
  { id: "m2", name: "Meteor Meatball Sub", price: 8.75, icon: "☄️" },
  { id: "m3", name: "Quantum Quiche", price: 6.20, icon: "🥧" },
  { id: "m4", name: "Void Water", price: 1.0, icon: "💧" },
  { id: "m5", name: "Supernova Sundae", price: 5.50, icon: "🍨" },
  { id: "m6", name: "Galactic Greens", price: 7.25, icon: "🥗" }
];

// Array to hold cart items
let cart = [];
let cartTotal = 0.0;

// --- 2. DOM Elements ---
const menuContainer = document.getElementById("menu-container");
const cartItemsList = document.getElementById("cart-items");
const totalPriceDisplay = document.getElementById("total-price");
const toast = document.getElementById("toast");

// --- 3. Flow Control & Logic ---
// Initialize the menu on load
function initMenu() {
  menu.forEach((item) => {
    // Create a div for the item
    const itemDiv = document.createElement("div");
    itemDiv.className = "menu-item";
    itemDiv.innerHTML = `
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">${item.icon}</div>
          <h3>${item.name}</h3>
          <p>$${item.price.toFixed(2)}</p>
          <button onclick="addToCart('${item.id}')">Add to Tray</button>
      `;
    menuContainer.appendChild(itemDiv);
  });
}

// Function to handle adding items
function addToCart(itemId) {
  // Find the item in our menu data
  const selectedItem = menu.find((item) => item.id === itemId);

  if (selectedItem) {
    // Generate a unique ID for the cart item instance so we can remove it specifically
    const cartItemInstance = { ...selectedItem, cartId: Date.now() + Math.random() };
    cart.push(cartItemInstance);
    cartTotal += selectedItem.price;
    updateCartDisplay();
  }
}

// Function to handle removing items
function removeFromCart(cartId) {
    const itemIndex = cart.findIndex(item => item.cartId === cartId);
    if (itemIndex > -1) {
        cartTotal -= cart[itemIndex].price;
        cart.splice(itemIndex, 1);
        
        // Prevent floating point precision issues
        if (cartTotal < 0 || cart.length === 0) cartTotal = 0;
        
        updateCartDisplay();
    }
}

// Function to update the screen
function updateCartDisplay() {
  // Clear the current list
  cartItemsList.innerHTML = "";

  if (cart.length === 0) {
      cartItemsList.innerHTML = '<li style="color: rgba(255,255,255,0.5); text-align: center; padding: 1rem 0;">Your tray is empty</li>';
  } else {
      // Re-render the cart list
      cart.forEach((item) => {
        const li = document.createElement("li");
        li.className = "cart-item";
        li.innerHTML = `
            <span>${item.icon} ${item.name}</span>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="font-weight: 600;">$${item.price.toFixed(2)}</span>
                <button class="remove-btn" onclick="removeFromCart(${item.cartId})">X</button>
            </div>
        `;
        cartItemsList.appendChild(li);
      });
  }

  // Update total price
  totalPriceDisplay.innerText = cartTotal.toFixed(2);
}

// Function for checkout
function checkout() {
    if (cart.length === 0) {
        alert("Your tray is empty! Please add items before checking out.");
        return;
    }
    
    // Show toast notification
    toast.innerHTML = `🚀 Order processed for $${cartTotal.toFixed(2)}!`;
    toast.classList.add("show");
    
    // Hide toast after 3 seconds
    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
    
    // Clear cart
    cart = [];
    cartTotal = 0.0;
    updateCartDisplay();
}

// Run init
initMenu();
