// components/Layout.tsx
'use client';
import { ReactNode } from 'react';
import Head from 'next/head';
import styles from './Layout.module.css';
import SolarSystem from './SolarSystem';
import { useEffect, useState } from 'react';
import Splash from './Splash';


type LayoutProps = {
  children: ReactNode;
};

const Layout = ({ children }: LayoutProps) => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Set a timeout to hide the loader after 3 seconds
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 5000); // 3000ms = 3 seconds

    // Clean up the timeout if the component is unmounted before the timeout is triggered
    return () => clearTimeout(timer);
  }, []);


  return (
    <div className={styles.container}>
      <Head>
        <title>ISRO-Lunar Map Project</title>
        <meta name="description" content="Lunar Map Project using XRF data" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {isLoading && (
        <div className='w-full h-full'>
          <Splash />
        </div>
      )
      }{
        !isLoading && (
          <div className='w-full h-full'>
            <SolarSystem />
            <header className={styles.header}>
              <h1>ISRO - Lunar Map Project - Inter-IIT</h1>
            </header>
            <main className={styles.main}>{children}</main>

          </div>
        )
      }

      <footer className={styles.footer}>
        <p>&copy; 2024 - Inter IIT- Lunar Map Project</p>
      </footer>

    </div>
  );
};

export default Layout;