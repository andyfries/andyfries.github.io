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

  // Add a "#" link to each post heading so readers can link to a section
  function addHeadingAnchors() {
    var post = document.querySelector('.post');
    if (!post) return;

    var headings = post.querySelectorAll('h1:not(.post-title), h2, h3, h4');
    headings.forEach(function(heading) {
      if (!heading.id) return;

      var anchor = document.createElement('a');
      anchor.className = 'heading-anchor';
      anchor.href = '#' + heading.id;
      anchor.setAttribute('aria-label', 'Link to section: ' + heading.textContent);
      anchor.textContent = '#';
      heading.appendChild(anchor);
    });
  }

  function init() {
    // TOC reads heading text, so build it before anchors add a "#"
    generateTOC();
    addHeadingAnchors();
  }

  // Run after DOM is loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})(document);
