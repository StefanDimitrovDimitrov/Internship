    // function addEventListener() {
    //     document.getElementById('main').addEventListener('click', e => {
    //         if (e.target.tagName == 'BUTTON') {
    //             const profile = e.target.parentNode;
    //             const isLocked = profile.querySelector('input[type=radio]:checked').value === 'lock'
    //
    //             if (isLocked) {
    //                 return;
    //             }
    //
    //             let div = profile.querySelector('div');
    //             let isVisible = div.style.display === 'block';
    //             div.style.display = isVisible ? 'none' : 'block';
    //             console.log(e.target)
    //             e.target.textContent = !isVisible ? 'Hide it' : 'Show more'
    //         }
    //     })
    // }