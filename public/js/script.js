(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');

  document.addEventListener('click', function(e) {
    var target = e.target;

    if(!checkbox.checked ||
       sidebar.contains(target) ||
       (target === checkbox || target === toggle)) return;

    checkbox.checked = false;
  }, false);

  // Generate table of contents
  function generateTOC() {
    var tocList = document.getElementById('toc-list');
    if (!tocList) return;

    var post = document.querySelector('.post');
    if (!post) return;

    var headings = post.querySelectorAll('h1:not(.post-title), h2, h3, h4');
    if (headings.length === 0) {
      var tocSidebar = document.querySelector('.toc-sidebar');
      if (tocSidebar) tocSidebar.style.display = 'none';
      return;
    }

    headings.forEach(function(heading, index) {
      // Add ID to heading if it doesn't have one
      if (!heading.id) {
        heading.id = 'heading-' + index;
      }

      var li = document.createElement('li');
      li.className = 'toc-' + heading.tagName.toLowerCase();

      var a = document.createElement('a');
      a.href = '#' + heading.id;
      a.textContent = heading.textContent;

      li.appendChild(a);
      tocList.appendChild(li);
    });
  }

  // Run after DOM is loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', generateTOC);
  } else {
    generateTOC();
  }
})(document);
