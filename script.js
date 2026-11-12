document.addEventListener('DOMContentLoaded', () => {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const forms = document.querySelectorAll('.auth-form');

  // Tab switching
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const target = button.dataset.tab;

      tabButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');

      forms.forEach(form => {
        form.classList.remove('active');
        if (form.id === `${target}-form`) {
          form.classList.add('active');
        }
      });
    });
  });

  // Sign In form
  const signinForm = document.getElementById('signin-form');
  const signinMessage = document.getElementById('signin-message');

  signinForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('signin-email').value;
    const password = document.getElementById('signin-password').value;

    // Simple client-side demo only
    if (email && password.length >= 6) {
      signinMessage.textContent = `Welcome back! (Demo — no real login)`;
      signinMessage.className = 'message success';
    } else {
      signinMessage.textContent = 'Please enter a valid email and password (min 6 chars).';
      signinMessage.className = 'message error';
    }
  });

  // Sign Up form
  const signupForm = document.getElementById('signup-form');
  const signupMessage = document.getElementById('signup-message');

  signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('signup-name').value.trim();
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    const confirm = document.getElementById('signup-confirm').value;

    if (!name || !email || !password) {
      signupMessage.textContent = 'Please fill in all fields.';
      signupMessage.className = 'message error';
      return;
    }

    if (password !== confirm) {
      signupMessage.textContent = 'Passwords do not match.';
      signupMessage.className = 'message error';
      return;
    }

    if (password.length < 8) {
      signupMessage.textContent = 'Password must be at least 8 characters.';
      signupMessage.className = 'message error';
      return;
    }

    signupMessage.textContent = `Account created for ${name}! (Demo only)`;
    signupMessage.className = 'message success';
    signupForm.reset();
  });
});
