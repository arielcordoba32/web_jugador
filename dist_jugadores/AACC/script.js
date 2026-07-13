// Función para abrir la foto en grande
function abrirFoto(src) {
  const modal = document.getElementById("lightbox-modal");
  const modalImg = document.getElementById("lightbox-img");

  modal.style.display = "flex";
  modalImg.src = src;
}

// Función para cerrar la foto
function cerrarFoto() {
  const modal = document.getElementById("lightbox-modal");
  modal.style.display = "none";
}

// Cerrar también si hacen clic en cualquier parte negra del fondo
document
  .getElementById("lightbox-modal")
  .addEventListener("click", function (e) {
    if (e.target !== document.getElementById("lightbox-img")) {
      cerrarFoto();
    }
  });
document.addEventListener("DOMContentLoaded", () => {
  // Initialize Lucide Icons
  if (typeof lucide !== "undefined") {
    lucide.createIcons();
  }

  // Navigation Menu Elements
  const menuToggle = document.getElementById("menuToggle");
  const navMenu = document.getElementById("navMenu");
  const navLinks = document.querySelectorAll(".nav-link");
  const navbar = document.querySelector(".navbar");

  // Toggle Mobile Menu
  if (menuToggle && navMenu) {
    menuToggle.addEventListener("click", () => {
      navMenu.classList.toggle("open");

      // Toggle Lucide Icon between menu and x
      const icon = menuToggle.querySelector("i");
      if (icon) {
        const isOpened = navMenu.classList.contains("open");
        icon.setAttribute("data-lucide", isOpened ? "x" : "menu");
        lucide.createIcons();
      }
    });
  }

  // Close Menu on Link Click
  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (navMenu) {
        navMenu.classList.remove("open");
      }
      const icon = menuToggle?.querySelector("i");
      if (icon) {
        icon.setAttribute("data-lucide", "menu");
        lucide.createIcons();
      }
    });
  });

  // Navbar Scroll Class
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar?.classList.add("scrolled");
    } else {
      navbar?.classList.remove("scrolled");
    }
  });

  // Scroll Animation - Intersection Observer
  const animateElements = document.querySelectorAll(".animate-box");
  const animationObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");

          // If it contains skill bars, animate them
          const skillFills = entry.target.querySelectorAll(".skill-fill");
          if (skillFills.length > 0) {
            skillFills.forEach((fill) => {
              // The CSS has a transition on width, so setting this triggers it
              // The inline style width is already defined in HTML but we can reinforce or animate
              const targetWidth = fill.style.width;
              fill.style.width = "0";
              setTimeout(() => {
                fill.style.width = targetWidth;
              }, 100);
            });
          }

          observer.unobserve(entry.target); // Stop observing after animation triggers
        }
      });
    },
    {
      threshold: 0.15,
      rootMargin: "0px 0px -50px 0px",
    },
  );

  animateElements.forEach((element) => {
    animationObserver.observe(element);
  });

  // Active Nav Link Observer
  const sections = document.querySelectorAll("section[id]");
  const navObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const currentId = entry.target.getAttribute("id");
          navLinks.forEach((link) => {
            link.classList.remove("active");
            if (link.getAttribute("href") === `#${currentId}`) {
              link.classList.add("active");
            }
          });
        }
      });
    },
    {
      threshold: 0.5,
      rootMargin: "-70px 0px -50% 0px",
    },
  );

  sections.forEach((section) => {
    navObserver.observe(section);
  });
});
