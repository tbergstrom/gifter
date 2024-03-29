/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './apps/logreg/templates/**/*.html',
    './apps/wishlist/templates/**/*.html',
  ] 
  ,
  darkMode: 'media', // or 'media' or 'class'
  theme: {
    extend: {
      backgroundColor: {
        'gray-50': '#F9FAFB',
        'gray-100': '#F3F4F6',
        'gray-200': '#E5E7EB',
        'gray-300': '#D1D5DB',
        'gray-400': '#9CA3AF',
        'gray-500': '#6B7280',
        'gray-600': '#4B5563',
        'gray-700': '#374151',
        'gray-800': '#1F2937',
        'gray-900': '#111827'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

