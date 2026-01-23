import sqlite3
import sys

def read_sqlite(db_file):
    try:
        # 连接到 SQLite 数据库
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print(f"✅ 成功连接到数据库: {db_file}\n")

        # 获取所有表名
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("⚠️ 数据库中没有找到任何表。")
            return

        print("📊 数据库中的表:")
        for idx, table in enumerate(tables, start=1):
            print(f"{idx}. {table[0]}")
        print("\n" + "="*50 + "\n")

        # 遍历每张表，显示前5行数据
        for table_name in tables:
            # if str(table_name[0]) not in "user":
            #     continue
            table = table_name[0]
            print(f"📋 表名: {table}")
            try:
                cursor.execute(f"SELECT * FROM {table};")
                rows = cursor.fetchall()

                # 获取列名
                column_names = [description[0] for description in cursor.description]
                print(f"   列: {column_names}")
                
                if rows:
                    for row in rows:
                        print(f"   {row}")
                else:
                    print("   (此表为空)")
            except Exception as e:
                print(f"   ❌ 读取表 {table} 时出错: {e}")
            print()

    except sqlite3.Error as e:
        print(f"❌ 数据库错误: {e}")
    except FileNotFoundError:
        print(f"❌ 数据库文件未找到: {db_file}")
    except Exception as e:
        print(f"❌ 发生错误: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("🔌 数据库连接已关闭。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("📌 用法: python read_sqlite.py <数据库文件路径>")
    else:
        db_path = sys.argv[1]
        read_sqlite(db_path)