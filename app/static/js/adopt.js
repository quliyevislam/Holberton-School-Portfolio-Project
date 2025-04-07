document.addEventListener('DOMContentLoaded', function() {
    // Set current year in footer
    document.getElementById('currentYear').textContent = new Date().getFullYear();
    
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function() {
        mobileMenu.classList.toggle('open');
      });
    }
    
    // Filter toggle on mobile
    const filterToggle = document.getElementById('filterToggle');
    const filterContainer = document.getElementById('filterContainer');
    
    if (filterToggle && filterContainer) {
      filterToggle.addEventListener('click', function() {
        filterContainer.classList.toggle('active');
        filterToggle.innerHTML = filterContainer.classList.contains('active') 
          ? '<i class="fas fa-times"></i> Hide Filters' 
          : '<i class="fas fa-filter"></i> Show Filters';
      });
    }
    
    // Reset filters
    const resetFilters = document.getElementById('resetFilters');
    
    if (resetFilters) {
      resetFilters.addEventListener('click', function() {
        document.querySelectorAll('.filter-select, .filter-input').forEach(function(input) {
          input.value = '';
        });
      });
    }
    
    // Apply filters (in a real app this would filter the animals)
    const applyFilters = document.getElementById('applyFilters');
    
    if (applyFilters) {
      applyFilters.addEventListener('click', function() {
        alert('Filters applied! In a real application, this would filter the animals based on your selection.');
      });
    }
    
    // Render report cards from localStorage (data provided via report.html submissions)
    function renderReportCards() {
      const reports = JSON.parse(localStorage.getItem('animalReports') || '[]');
      const reportCardsContainer = document.getElementById('reportCards');
      reportCardsContainer.innerHTML = '';
      
      if (reports.length === 0) {
        reportCardsContainer.innerHTML = '<p>No reports submitted yet.</p>';
        return;
      }
      
      reports.forEach(report => {
        // Create a report card element
        const card = document.createElement('div');
        card.className = 'report-card';
        card.innerHTML = `
          <div class="report-header">${report.animalType ? report.animalType.toUpperCase() : 'Unknown Animal'}</div>
          <div class="report-meta">
            <strong>Reported by:</strong> ${report.name || 'Anonymous'}<br>
            <strong>Contact:</strong> ${report.contact || 'N/A'}<br>
            <strong>Found at:</strong> ${report.location || 'Unknown'}<br>
            <strong>Date:</strong> ${report.dateFound || ''}
          </div>
          <a href="report.html?id=${report.id}" class="view-report">View Details</a>
        `;
        reportCardsContainer.appendChild(card);
      });
    }
    
    renderReportCards();
  });