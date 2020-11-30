const template = document.getElementById("cs-demo-template");

class CsDemo extends HTMLElement {
  constructor() {
    super();

    const shadow = this.attachShadow({mode: "open"});
    shadow.appendChild(template.content.cloneNode(true));
  }

  connectedCallback() {
    console.debug("CsDemo added to DOM.");

    this.shadowRoot.addEventListener("click", e => {
      if (e.target.hasAttribute("rating")) {
        console.debug(`CsDemo clicked, rating: ${e.target.getAttribute("rating")}`);
      }
    });
  }

  adoptedCallback() {
    console.debug("CsDemo was moved into a new part of the DOM.");
  }

  disconnectedCallback() {
    console.debug("CsDemo was removed from the DOM.");
  }

  static get observedAttributes() {
    return ['rating'];
  }

  attributeChangedCallback(name, oldVal, newVal) {
    if (oldVal !== newVal) {
      console.debug(`CsDemo attribute changed: [${name}] ${oldVal} => ${newVal}`);
    }
  }

  get rating() {
    return +this.getAttribute("rating") || 0;
  }

  set rating(rating) {
    this.setAttribute("rating", rating);
  }
}

customElements.define("cs-demo", CsDemo);

export default CsDemo;
