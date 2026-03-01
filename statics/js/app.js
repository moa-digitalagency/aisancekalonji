        // --- LOGIQUE DARK / LIGHT MODE ---
        const themeToggleBtn = document.getElementById('theme-toggle');
        const htmlElement = document.documentElement;

        // Vérifier le thème sauvegardé
        if (localStorage.getItem('theme') === 'light') {
            htmlElement.classList.remove('dark');
        } else {
            htmlElement.classList.add('dark'); // Sombre par défaut
        }

        themeToggleBtn.addEventListener('click', () => {
            htmlElement.classList.toggle('dark');
            if (htmlElement.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });

        // --- MENU MOBILE HAMBURGER ---
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileIcon = mobileBtn.querySelector('i');
        const mobileLinks = document.querySelectorAll('.mobile-link');

        function toggleMenu() {
            const isHidden = mobileMenu.classList.contains('invisible');
            if (isHidden) {
                // Ouvrir
                mobileMenu.classList.remove('invisible', 'opacity-0', '-translate-y-4');
                mobileMenu.classList.add('opacity-100', 'translate-y-0');
                mobileIcon.classList.remove('fa-bars');
                mobileIcon.classList.add('fa-times');
            } else {
                // Fermer
                mobileMenu.classList.add('invisible', 'opacity-0', '-translate-y-4');
                mobileMenu.classList.remove('opacity-100', 'translate-y-0');
                mobileIcon.classList.remove('fa-times');
                mobileIcon.classList.add('fa-bars');
            }
        }

        mobileBtn.addEventListener('click', toggleMenu);
        mobileLinks.forEach(link => link.addEventListener('click', toggleMenu));

        // --- GESTION DROPDOWN LANGUES ---
        const langToggleBtn = document.getElementById('lang-toggle');
        const langDropdown = document.getElementById('lang-dropdown');
        const currentLangFlag = document.getElementById('current-lang-flag');
        const langOptions = document.querySelectorAll('.lang-option');

        // Ouvrir/Fermer au clic sur le bouton
        langToggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isHidden = langDropdown.classList.contains('invisible');
            if (isHidden) {
                langDropdown.classList.remove('invisible', 'opacity-0', 'translate-y-2');
                langDropdown.classList.add('opacity-100', 'translate-y-0');
            } else {
                langDropdown.classList.add('invisible', 'opacity-0', 'translate-y-2');
                langDropdown.classList.remove('opacity-100', 'translate-y-0');
            }
        });

        // Fermer le menu si on clique en dehors
        document.addEventListener('click', (e) => {
            if (!langToggleBtn.contains(e.target) && !langDropdown.contains(e.target)) {
                langDropdown.classList.add('invisible', 'opacity-0', 'translate-y-2');
                langDropdown.classList.remove('opacity-100', 'translate-y-0');
            }
        });

        // Changement de drapeau au clic sur une langue
        langOptions.forEach(option => {
            option.addEventListener('click', () => {
                // MISE À JOUR : On récupère uniquement le drapeau via l'attribut data-flag
                currentLangFlag.textContent = option.getAttribute('data-flag');

                langDropdown.classList.add('invisible', 'opacity-0', 'translate-y-2');
                langDropdown.classList.remove('opacity-100', 'translate-y-0');

                // Ici viendra la future logique pour changer la langue du site
                // const selectedLang = option.getAttribute('data-lang');
                // changeLanguage(selectedLang);
            });
        });

        // --- 1. SÉQUENCE PRELOADER ---
        document.addEventListener("DOMContentLoaded", () => {
            const tl = gsap.timeline();

            tl.to("#t1", {opacity: 1, y: -10, duration: 0.4, delay: 0.3})
              .to("#t2", {opacity: 1, y: -10, duration: 0.4, delay: 0.2})
              .to("#t3", {opacity: 1, y: -10, duration: 0.4, delay: 0.2})
              .to("#t4", {opacity: 1, duration: 0.5, delay: 0.4})
              .to("#preloader", {
                  opacity: 0,
                  duration: 1,
                  ease: "power2.inOut",
                  delay: 0.5,
                  onComplete: () => {
                      document.getElementById('preloader').style.display = 'none';
                      initMainAnimations();
                  }
              });
        });

        // --- 2. SMOOTH SCROLL (LENIS) ---
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            smooth: true,
        });

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time)=>{ lenis.raf(time * 1000); });
        gsap.ticker.lagSmoothing(0, 0);

        // --- 3. ANIMATIONS GSAP & PARALLAX ---
        function initMainAnimations() {
            gsap.registerPlugin(ScrollTrigger);

            // Entrée du texte Hero
            gsap.from(".gs-hero-text > *", {
                y: 30, opacity: 0, duration: 1, stagger: 0.1,
                ease: "power3.out", clearProps: "all"
            });

            // Entrée de l'image Hero
            gsap.from(".gs-hero-img", {
                scale: 0.95, opacity: 0, duration: 1.5, delay: 0.4,
                ease: "power3.out", clearProps: "all"
            });

            // Parallax sur les images
            gsap.utils.toArray('.img-mask').forEach(container => {
                const img = container.querySelector('.img-parallax');
                if (img) {
                    const speed = img.getAttribute('data-speed') || 0.9;
                    gsap.to(img, {
                        yPercent: (1 - parseFloat(speed)) * 50,
                        ease: "none",
                        scrollTrigger: {
                            trigger: container, start: "top bottom",
                            end: "bottom top", scrub: true
                        }
                    });
                }
            });

            // Reveal au défilement
            gsap.utils.toArray('.gs-reveal').forEach(elem => {
                gsap.fromTo(elem,
                    { y: 40, opacity: 0 },
                    {
                        y: 0, opacity: 1, duration: 1, ease: "power2.out",
                        scrollTrigger: { trigger: elem, start: "top 85%" }
                    }
                );
            });
        }
