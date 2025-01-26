import Earth from "./earth"
import './splash.css'
const Splash = () => {

    return(
    <div className="splash">
        <h1>ISRO-Lunar Map Project</h1>
        <Earth></Earth>
        <img  className= 'bg' src="/img/spacebg.jpg" alt="bg" />
    </div>
    )

}
export default Splash;
