/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

const plugin = require('tailwindcss/plugin')
const colors = require("tailwindcss/colors")

module.exports = {
    content: [
        '../../Blog/templates/Blog/**/*.html',
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../**/*.py',
    ],
    darkMode: 'media',
    theme: {
        extend: {
            colors: {
                primary: '#FFE5E5',
                contrast: '#756AB6',
                third: '#AC87C5',
                fourth: '#E0AED0',
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        plugin(function ({ addComponents, addBase}) {
            addBase({
                'img': { 
                    maxWidth: '50rem',
                },
                'textarea': {
                    margin: '2rem 0',
                },
                'hr': {
                    width: '66%',
                    height: '0.1rem',
                    margin: '2rem 0',
                    border: 'none',
                    borderRadius: '100%',
                    backgroundColor: '#FFE5E5',
                },
                'p': {
                    marginTop: '1rem',
                },
                'a': {
                    color: '#756AB6',
                    textDecoration: 'none',
                    '&:hover': {
                        color: '#4C2C59',
                    },
                }
            })
            addComponents({
                '.container': {
                    borderRadius: '0.5rem',
                    boxShadow: '0 0 10px rgba(0,0,0,0.1)',
                    overflow: 'hidden',
                    backgroundColor: 'white',
                    padding: '1rem',
                    margin: '1rem 0',
                },
                '.send-button': {
                    color: '#734D8C',
                    aspectRatio: '1',
                    scale: '1',
                    transition: 'all 0.3s',
                    transitionTimingFunction: 'ease-in-out',
                    cursor: 'pointer',
                    '&:hover': {
                        scale: '1.1',
                        color: '#756AB6',
                    }
                },
                '.transition-card': {
                    transition: 'all 0.3s',
                    transitionTimingFunction: 'ease-in-out',
                    cursor: 'pointer',
                    scale: '1',
                    '&:hover': {
                        boxShadow: '0 0 10px rgba(0,0,0,0.2)',
                        scale: '1.05',
                    },
                },
                '.transition-btn': {
                    transition: 'all 0.3s',
                    transitionTimingFunction: 'ease-in-out',
                    cursor: 'pointer',
                    '&:hover': {
                        backgroundColor: '#4C2C59',
                    },
                },
                '.hov-txt': {
                    transition: 'all 0.3s',
                    transitionTimingFunction: 'ease-in-out',
                    cursor: 'pointer',
                    color: 'white',
                    borderBottom: '2px solid transparent',
                    '&:hover': {
                        color: 'gray-300',
                        borderBottom: '2px solid #4C2C59',
                    },
                },
                '.title-container': {
                    display: 'flex',
                    flexDirection: 'row',
                    justifyContent: 'center',
                    alignItems: 'center',
                },
                '.title': {
                    fontSize: '2rem',
                    fontWeight: 'bold',
                    color: '#734D8C',
                    textAlign: 'center',
                    width: '100%',
                },
            })
        })
    ],
}
