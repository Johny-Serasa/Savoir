document.addEventListener('DOMContentLoaded', function() {
  const items = document.querySelectorAll('.carousel-item');
  const prevBtn = document.querySelector('.carousel-btn.prev');
  const nextBtn = document.querySelector('.carousel-btn.next');

  if (!items.length || !prevBtn || !nextBtn) {
    console.error('Carousel elements not found');
    return;
  }

  let currentIndex = 0;

  // Show first item
  items[currentIndex].classList.add('active');

  function showItem(index) {
    items.forEach(item => item.classList.remove('active'));
    items[index].classList.add('active');
  }

  nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % items.length;
    showItem(currentIndex);
  });

  prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    showItem(currentIndex);
  });

  console.log('Carousel initialized with', items.length, 'items');
});
