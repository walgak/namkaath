// --- 1. Theme Toggle Logic ---
const themeToggle = document.getElementById('themeToggle');
const body = document.body;
const icon = themeToggle.querySelector('i');

// Check local storage or default to dark
const savedTheme = localStorage.getItem('theme') || 'light';
body.setAttribute('data-theme', savedTheme);
updateIcon(savedTheme);

themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateIcon(newTheme);
});

function updateIcon(theme) {
    if (theme === 'dark') {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    }
}

// --- 2. Navbar Scroll Effect ---
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// --- 3. Scroll Animations (Intersection Observer) ---
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
});

// --- 4. Mobile Menu Toggle ---
const mobileBtn = document.getElementById('mobileMenu');
const navLinks = document.getElementById('navLinks');

mobileBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    const icon = mobileBtn.querySelector('i');
    if (navLinks.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-xmark');
    } else {
        icon.classList.remove('fa-xmark');
        icon.classList.add('fa-bars');
    }
});

// Close menu when clicking a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        mobileBtn.querySelector('i').classList.remove('fa-xmark');
        mobileBtn.querySelector('i').classList.add('fa-bars');
    });
});

// --- 5. SMOOTH PHYSICS ANIMATION ENGINE ---

const svg = document.getElementById('neural-network');
// Use 800x600 as base coordinate system (matching viewBox)
const width = 800;
const height = 600;
const nodeCount = 40; 
const nodes = [];
let lines = [];

class Node {
    constructor() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        // Very slow velocity for smooth drift
        this.vx = (Math.random() - 0.5) * 0.2; 
        this.vy = (Math.random() - 0.5) * 0.2;
        this.radius = 2 + Math.random() * 3;
        
        this.element = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        this.element.setAttribute("r", this.radius);
        this.element.classList.add("neural-node");
        this.element.style.fill = "var(--node-color)";
        svg.appendChild(this.element);
    }

    update() {
        // Move
        this.x += this.vx;
        this.y += this.vy;

        // Bounce off edges
        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;

        // Update SVG position
        this.element.setAttribute("cx", this.x);
        this.element.setAttribute("cy", this.y);
    }
}

function init() {
    // Create Nodes
    for (let i = 0; i < nodeCount; i++) {
        nodes.push(new Node());
    }
    animate();
}

function animate() {
    // 1. Update Node Positions
    nodes.forEach(node => node.update());

    // 2. Draw Lines
    // First, remove old lines
    lines.forEach(line => line.remove());
    lines = [];

    // Brute force distance check (optimized for small N=40)
    for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
            const dx = nodes[i].x - nodes[j].x;
            const dy = nodes[i].y - nodes[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < 120) { // Connection distance threshold
                const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                line.setAttribute("x1", nodes[i].x);
                line.setAttribute("y1", nodes[i].y);
                line.setAttribute("x2", nodes[j].x);
                line.setAttribute("y2", nodes[j].y);
                line.classList.add("neural-line");
                line.style.stroke = "var(--line-color)";
                
                // Fade out line based on distance
                const opacity = 1 - (dist / 120);
                line.style.opacity = opacity * 0.5; 

                // Insert before nodes so dots are on top
                svg.insertBefore(line, nodes[0].element); 
                lines.push(line);
            }
        }
    }

    requestAnimationFrame(animate);
}

// Initialize on load
window.addEventListener('DOMContentLoaded', init);