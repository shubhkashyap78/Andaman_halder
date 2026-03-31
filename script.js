window.addEventListener('load', () => {
  setTimeout(() => document.getElementById('loader').classList.add('hidden'), 2000);
});

const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');
let mx = 0, my = 0, rx = 0, ry = 0;
document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.transform = `translate(${mx-5}px,${my-5}px)`;
});
(function animRing() {
  rx += (mx - rx - 18) * 0.12;
  ry += (my - ry - 18) * 0.12;
  ring.style.transform = `translate(${rx}px,${ry}px)`;
  requestAnimationFrame(animRing);
})();

window.addEventListener('scroll', () => {
  document.getElementById('navbar').classList.toggle('scrolled', scrollY > 50);
});

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-in,.fade-left,.fade-right').forEach(el => obs.observe(el));

const cObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting && !e.target.dataset.done) {
      e.target.dataset.done = 1;
      const target = +e.target.dataset.count;
      let n = 0; const step = target / 120;
      const t = setInterval(() => {
        n = Math.min(n + step, target);
        e.target.textContent = Math.floor(n) + '+';
        if (n >= target) clearInterval(t);
      }, 16);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => cObs.observe(el));

function handleSubmit(e) {
  e.preventDefault();
  const btn = document.getElementById('submitBtn');
  btn.textContent = 'Sending...';
  btn.style.background = '#888';
  setTimeout(() => {
    btn.textContent = '✓ Enquiry Sent!';
    btn.style.background = '#2a7a4b';
    setTimeout(() => { btn.textContent = 'Send Enquiry'; btn.style.background = ''; e.target.reset(); }, 3000);
  }, 1500);
}
