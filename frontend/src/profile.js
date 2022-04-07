import React from 'react'
import Navbar2 from './navbar2.js'
import Content from './Content.js'
import TimeSeries from './TimeSeries.js'
import Performance from './Performance.js'
import Tweet from './Tweet.js'
// import Sentiments from './Sentiments.js'
// import Footer from './Footer.js'
import Fundamental from './fundamental.js'
import CompanyLogo from './CompanyLogo.js'
import './profile.css'

function Profile() {

  const tweets  = Content["tweet_ids"];
  // const id = Object.keys(tweets);
  // const sentiment = Object.values(tweets);
  // const { dates,dates_data } = alpha_vantage;

  return (
       <div className="Profile">
          <Navbar2 />
          <div className="data">
          <div className="CompanyLogo">
            <CompanyLogo />
          </div>
          <div className="TimeSeries">
            <TimeSeries />
          </div>
          <div className="performance">
            <Performance />
          </div>
          <div className="fundamental">
            <Fundamental />
          </div>
          <div className="twitter_embedding">
            <h2>Trending Tweets</h2>
            {Object.keys(tweets).slice(0,5).map((item) => (
              <Tweet
                id={item}
                tweet_id={item}
                sent={tweets[item]}
              />
            ))}
          </div>
          <div className="footer">
              {/* <Footer /> */}
          </div>
        </div>
       </div>
  )
}

export default Profile

// {Content.map((item) => {
//   return (<>
//   <h1>{item.name}</h1>
//   <p>{item.content}</p>
//   <p>{item.finance}</p>
//   <p>{item.chart_data}</p>
//   </>)
// })}


              {/* <div className="left-content">
                <div className="centerContent">
                  <div className="selfCenter spaceBetween">
                    <TwitterTweetEmbed
                      onLoad={function noRefCheck(){}}
                      placeholder={<div style={{backgroundColor: 'red', color: 'white', margin: 10, padding: 10}}>Hello I am custom placeholder</div>}
                      tweetId="1083592734038929408"
                    />
                  </div>
                </div>
              </div>ᐧ */}



{/* <ChangingProgressProvider values={[0, 20, 80]}>
        {value => (
          <CircularProgressbar
            value={value}
            text={`${value}%`}
            circleRatio={0.75}
            styles={buildStyles({
              rotation: 1 / 2 + 1 / 8,
              strokeLinecap: "butt",
              trailColor: "#eee"
            })}
          />
        )}
      </ChangingProgressProvider> */}